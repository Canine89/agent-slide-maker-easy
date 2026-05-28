# HyperFrames Composition Project

## Skills — USE THESE FIRST

**Always invoke the relevant skill before writing or modifying compositions.** Skills encode framework-specific patterns (e.g., `window.__timelines` registration, `data-*` attribute semantics, shader-compatible CSS rules) that are NOT in generic web docs. Skipping them produces broken compositions.

| Skill               | Command            | When to use                                                                                       |
| ------------------- | ------------------ | ------------------------------------------------------------------------------------------------- |
| **hyperframes**     | `/hyperframes`     | Creating or editing HTML compositions, captions, TTS, audio-reactive animation, marker highlights |
| **hyperframes-cli** | `/hyperframes-cli` | CLI commands: init, lint, preview, render, transcribe, tts                                        |
| **gsap**            | `/gsap`            | GSAP animations for HyperFrames — tweens, timelines, easing, performance                          |

> **Skills not available?** Ask the user to run `npx hyperframes skills` and restart their
> agent session, or install manually: `npx skills add heygen-com/hyperframes`.

## Commands

```bash
npx hyperframes preview          # preview in browser (studio editor)
npx hyperframes render       # render to MP4
npx hyperframes lint         # validate compositions (errors + warnings)
npx hyperframes lint --verbose  # include info-level findings
npx hyperframes lint --json     # machine-readable output for CI
npx hyperframes docs <topic> # reference docs in terminal
```

## Documentation

**For quick reference**, use the local CLI docs command (no network required):

```bash
npx hyperframes docs <topic>
```

Topics: `data-attributes`, `gsap`, `compositions`, `rendering`, `examples`, `troubleshooting`

**For full documentation**, discover pages via the machine-readable index — do NOT guess URLs:

```
https://hyperframes.heygen.com/llms.txt
```

## Project Structure

이 프로젝트는 **주제별 서브프로젝트 패턴**을 쓴다. 루트는 워크스페이스, 실제 컴포지션은 `topics/<주제-이름>/` 안에 둔다.

```
lab-hyperframes/
├── .claude/skills                Claude Code용 스킬 심링크
├── .codex/skills/                Codex용 로컬 스킬 원본
├── .cursor/skills                Cursor용 스킬 심링크
├── PROJECT.md                    사용자 가이드 (전체 흐름 설명)
├── hyperframes.json, meta.json   워크스페이스 마커
├── topics/
│   ├── _template/                새 주제 시작용 뼈대 (복사해서 사용)
│   ├── openai-history/           개별 주제 = 독립된 hyperframes 프로젝트
│   └── <주제-이름>/
│       ├── hyperframes.json      (필수)
│       ├── meta.json             (필수 — name이 렌더 파일명에 반영됨)
│       ├── index.html            영상 소스 (GSAP 타임라인)
│       ├── static.html           정적 HTML 덱 (애니메이션 없음)
│       ├── assets/               주제 전용 이미지·폰트
│       ├── renders/              mp4 결과물
│       └── snapshots/            PNG 스냅샷
└── _archive/                     과거 테스트 산출물
```

**루트에는 composition용 index.html이 없다.** 루트에서 `npx hyperframes render` 하면 실패한다 — 반드시 주제 폴더를 지정해야 한다.

## Topic Workflow — 새 주제 만들 때

1. **템플릿 복사**: `cp -r topics/_template topics/<주제-이름>`
2. **meta.json 수정**: `topics/<주제-이름>/meta.json`의 `id`/`name`을 `<주제-이름>`으로 변경 — 렌더 파일명에 반영됨
3. **index.html 작성**: `.codex/skills/hyperframes-slide-work-*` 스킬을 참조해 슬라이드 타입별 HTML + GSAP 작성
4. **preview / render / snapshot** 모두 `topics/<주제-이름>` 경로를 타겟으로 실행

**절대 루트의 `index.html`, `assets/`, `renders/`에 파일을 만들지 말 것.** 모든 작업물은 해당 주제 폴더 안에 둔다.

## 주제별 CLI 호출 예시

```bash
npx hyperframes preview topics/openai-history    # 라이브 미리보기
npx hyperframes render  topics/openai-history    # mp4 렌더
npx hyperframes lint    topics/openai-history    # 린트
npx hyperframes snapshot topics/openai-history --at 2.5,8.1,13.7,...
```

## Linting — ALWAYS RUN AFTER CHANGES

After creating or editing any `.html` composition, **always** run the linter before considering the task complete:

```bash
npx hyperframes lint
```

Fix all errors before presenting the result. Warnings are informational and usually safe to ignore.

## Key Rules

1. Every timed element needs `data-start`, `data-duration`, and `data-track-index`
2. Elements with timing **MUST** have `class="clip"` — the framework uses this for visibility control
3. Timelines must be paused and registered on `window.__timelines`:
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
4. Videos use `muted` with a separate `<audio>` element for the audio track
5. Sub-compositions use `data-composition-src="compositions/file.html"` to reference other HTML files
6. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches
