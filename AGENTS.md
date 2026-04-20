# HyperFrames Composition Project

## Skills

This project uses AI agent skills for framework-specific patterns. Install them if not already present:

```bash
npx skills add heygen-com/hyperframes
```

Skills encode patterns like `window.__timelines` registration, `data-*` attribute semantics, and shader-compatible CSS rules that are not in generic web docs. Using them produces correct compositions from the start.

## Commands

```bash
npx hyperframes preview --port 3000      # preview in browser (studio editor) — ALWAYS on 3000
npx hyperframes render                    # render to MP4
npx hyperframes lint                      # validate compositions (errors + warnings)
npx hyperframes lint --json               # machine-readable output for CI
npx hyperframes docs <topic>              # reference docs in terminal
```

## Preview Port Rule — ALWAYS use port 3000

이 프로젝트의 preview 서버는 **항상 포트 3000**에서 실행한다. hyperframes 기본값은 3002지만, 이 규칙을 따른다.

**다른 프로세스가 3000을 점유하고 있으면 먼저 정리한다:**

```bash
# 1. 활성 hyperframes preview 서버 확인
npx hyperframes preview --list

# 2. 기존 hyperframes preview 전부 정리
npx hyperframes preview --kill-all

# 3. 3000번을 다른 프로세스가 점유 중인지 확인
lsof -nP -iTCP:3000 -sTCP:LISTEN

# 4. hyperframes 가 아니라면 PID로 종료 후 재시작
kill <PID>
npx hyperframes preview topics/<주제-이름> --port 3000
```

주제를 바꿔 새 preview를 띄울 때도 먼저 `--kill-all`로 기존 서버를 정리한 뒤 3000에서 재시작한다. 포트가 여러 개로 분산되지 않게 유지.

## Project Structure

- `index.html` — main composition (root timeline)
- `compositions/` — sub-compositions referenced via `data-composition-src`
- `assets/` — media files (video, audio, images)
- `meta.json` — project metadata (id, name)
- `transcript.json` — whisper word-level transcript (if generated)

## Linting — Always Run After Changes

After creating or editing any `.html` composition, run the linter before considering the task complete:

```bash
npx hyperframes lint
```

Fix all errors before presenting the result.

## Key Rules

1. Every timed element needs `data-start`, `data-duration`, and `data-track-index`
2. Visible timed elements **must** have `class="clip"` — the framework uses this for visibility control
3. GSAP timelines must be paused and registered on `window.__timelines`:
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
4. Videos use `muted` with a separate `<audio>` element for the audio track
5. Sub-compositions use `data-composition-src="compositions/file.html"`
6. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches

## Documentation

Full docs: https://hyperframes.heygen.com/introduction

Machine-readable index for AI tools: https://hyperframes.heygen.com/llms.txt
