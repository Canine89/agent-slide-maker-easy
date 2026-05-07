#!/usr/bin/env python3
"""
serve-live.py — static file server + POST /save endpoint that applies
overview-edit patches to the topic's index.html and overview.html in place.

Usage:
    python3 serve-live.py <topic-dir> [port]

Endpoint:
    POST /save  with body {"patch": "<markdown patch>"}
    Returns JSON: {"applied": N, "changes_requested": M, "files": {...}}

Fallback behavior:
    If POST fails (e.g., topic folder has no index.html), returns error JSON.
    Browser-side JS can fall back to clipboard copy.
"""
import json
import os
import re
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer

TOPIC_DIR = None  # set from argv


def parse_patch(patch_text):
    """Parse overview-edit patch markdown → list of change dicts."""
    changes = []
    lines = patch_text.split('\n')
    cur_num = None
    cur_kind = 'card'
    cur_sel = None
    reading = None
    old_buf, new_buf = [], []

    def flush():
        nonlocal cur_sel, old_buf, new_buf, reading
        if cur_sel is not None and old_buf and new_buf:
            changes.append({
                'card_num': cur_num,
                'card_kind': cur_kind,
                'selector': cur_sel,
                'old': '\n'.join(old_buf).strip(),
                'new': '\n'.join(new_buf).strip(),
            })
        cur_sel = None
        old_buf = []
        new_buf = []
        reading = None

    for line in lines:
        m = re.match(r'^## (Card|Slide) (\d+)', line)
        if m:
            flush()
            cur_kind = 'card' if m.group(1) == 'Card' else 'slide'
            cur_num = m.group(2)
            continue
        m = re.match(r'^- (\S+)', line)
        if m:
            flush()
            cur_sel = m.group(1)
            reading = None
            continue
        m = re.match(r'^\s+OLD: (.*)$', line)
        if m:
            reading = 'old'
            old_buf = [m.group(1)]
            continue
        m = re.match(r'^\s+NEW: (.*)$', line)
        if m:
            reading = 'new'
            new_buf = [m.group(1)]
            continue
        # multi-line continuation (rare but supported)
        if reading == 'old':
            old_buf.append(line)
        elif reading == 'new':
            new_buf.append(line)
    flush()
    return changes


def find_card_block(html, card_kind, card_num):
    """Return (start, end) offsets in html of the target card's <div> block."""
    if card_kind == 'card':
        attrs = [f'data-card="{card_num}"', f'id="c-{card_num}"']
    else:
        attrs = [f'data-slide="{card_num}"', f'id="s-{card_num}"']

    start = -1
    for a in attrs:
        idx = html.find(a)
        if idx != -1:
            div_idx = html.rfind('<div', 0, idx)
            if div_idx != -1:
                start = div_idx
                break
    if start == -1:
        return None, None

    # Find the start of the NEXT sibling card as the end anchor
    if card_kind == 'card':
        next_re = re.compile(r'<div\s[^>]*?(?:data-card="(\d+)"|id="c-(\d+)")')
    else:
        next_re = re.compile(r'<div\s[^>]*?(?:data-slide="(\d+)"|id="s-(\d+)")')

    end = len(html)
    for m in next_re.finditer(html, start + 4):
        num = m.group(1) or m.group(2)
        if num != card_num:
            end = m.start()
            break
    return start, end


def apply_change_to_html(html, change):
    """Apply one change. Returns (new_html, applied_bool)."""
    start, end = find_card_block(html, change['card_kind'], change['card_num'])
    if start is None:
        return html, False

    block = html[start:end]
    sel = change['selector']
    cls = sel[1:].split('.')[0] if sel.startswith('.') else None  # first class only

    if not cls:
        # tag-only fallback (rare)
        tag = sel.lower()
        pattern = re.compile(
            r'(<' + re.escape(tag) + r'[^>]*>)([\s\S]*?)(</' + re.escape(tag) + r'>)',
            re.DOTALL
        )
    else:
        pattern = re.compile(
            r'(<(\w+)[^>]*\bclass="[^"]*\b' + re.escape(cls) + r'\b[^"]*"[^>]*>)'
            r'([\s\S]*?)'
            r'(</\2>)',
            re.DOTALL
        )

    old_trimmed = change['old'].strip()
    new_text = change['new']

    replaced = {'count': 0}

    def replacer(match):
        if cls:
            open_tag = match.group(1)
            inner = match.group(3)
            close_tag = match.group(4)
        else:
            open_tag = match.group(1)
            inner = match.group(2)
            close_tag = match.group(3)
        if inner.strip() == old_trimmed and replaced['count'] == 0:
            replaced['count'] += 1
            # preserve any leading/trailing whitespace inside the tag
            lead_ws = inner[:len(inner) - len(inner.lstrip())]
            trail_ws = inner[len(inner.rstrip()):]
            return open_tag + lead_ws + new_text + trail_ws + close_tag
        return match.group(0)

    new_block = pattern.sub(replacer, block)
    if replaced['count'] == 0:
        return html, False
    return html[:start] + new_block + html[end:], True


class Handler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path != '/save':
            self.send_error(404, 'Unknown endpoint')
            return

        length = int(self.headers.get('Content-Length', 0))
        if length <= 0:
            self.send_error(400, 'Empty body')
            return

        raw = self.rfile.read(length).decode('utf-8', errors='replace')
        try:
            data = json.loads(raw)
            patch = data.get('patch', '')
        except Exception as e:
            self.send_error(400, f'Invalid JSON: {e}')
            return

        if not patch.strip():
            self._reply_json(200, {'applied': 0, 'changes_requested': 0, 'files': {}})
            return

        changes = parse_patch(patch)
        if not changes:
            self._reply_json(200, {'applied': 0, 'changes_requested': 0, 'files': {}})
            return

        applied = {}
        errors = []

        for fname in ('index.html', 'overview.html'):
            fpath = os.path.join(TOPIC_DIR, fname)
            if not os.path.isfile(fpath):
                continue
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    html = f.read()
            except Exception as e:
                errors.append(f'{fname}: read failed ({e})')
                continue

            count = 0
            for ch in changes:
                new_html, ok = apply_change_to_html(html, ch)
                if ok:
                    html = new_html
                    count += 1

            if count > 0:
                try:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(html)
                    applied[fname] = count
                except Exception as e:
                    errors.append(f'{fname}: write failed ({e})')

        total = sum(applied.values())
        response = {
            'applied': total,
            'changes_requested': len(changes),
            'files': applied,
        }
        if errors:
            response['errors'] = errors
        self._reply_json(200, response)

    def _reply_json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        sys.stderr.write('[serve-live] ' + (format % args) + '\n')


def main():
    global TOPIC_DIR
    if len(sys.argv) < 2:
        print('Usage: serve-live.py <topic-dir> [port]')
        sys.exit(1)
    TOPIC_DIR = os.path.abspath(sys.argv[1])
    if not os.path.isdir(TOPIC_DIR):
        print(f'Not a directory: {TOPIC_DIR}')
        sys.exit(1)
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8765
    os.chdir(TOPIC_DIR)
    server = HTTPServer(('', port), Handler)
    print(f'Serving {TOPIC_DIR} on http://localhost:{port}/overview.html')
    print(f'POST /save endpoint active — overview edits will be written to index.html + overview.html')
    print('Press Ctrl+C to stop.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n[serve-live] stopped')


if __name__ == '__main__':
    main()
