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

## Review Workflow — Overview First, Render Second (필수)

이 프로젝트의 리뷰 흐름은 **항상 오버뷰 먼저, 영상 렌더는 그 다음**이다.

1. 카드뉴스·슬라이드를 만들면 `topics/<주제>/overview.html` 을 생성한다
2. `bash .codex/skills/hyperframes-overview/serve.sh topics/<주제> <포트>` 로 live HTTP 서빙해 사용자에게 **오버뷰 URL을 먼저 제시**한다
3. 사용자가 내용을 검토하고 수정을 요청하면 반영 → 오버뷰 갱신 재검토
4. 사용자가 오버뷰 내용에 **명시적으로 OK** 하고 **영상을 요청**한 뒤에만 `npx hyperframes render` 를 실행한다

### 용어 충돌 — "프리뷰"라고 해도 오버뷰를 먼저 보여준다

사용자가 관습적으로 "프리뷰 보여줘", "preview로 확인" 이라고 말해도, 실제 의도는 대부분 **정적 오버뷰(overview.html)** 를 뜻한다. HyperFrames CLI 의 `preview` (studio editor, 포트 3000의 라이브 스크러버)는 다른 도구다.

**규칙**:
- 사용자가 "프리뷰", "preview", "미리보기" 라고 말해도 **오버뷰부터 만들어 보여준다**
- HyperFrames studio preview가 정말 필요한 건지 **확실할 때만** `npx hyperframes preview` 를 쓴다 (예: "studio 열어줘", "실시간으로 스크러빙 하고 싶어" 처럼 live timeline 편집 의도가 분명한 경우)
- **영상 만들지 말고 확인만**이라는 요청은 = **오버뷰만 띄워라** 라는 뜻이지 render 건너뛰고 studio 띄우라는 뜻이 아니다

### 언제 render를 해도 되나

아래 중 하나일 때만 `npx hyperframes render` 실행:
- 사용자가 "영상 만들어줘", "render 해줘", "mp4 뽑아줘" 라고 명시적으로 요청
- 이미 오버뷰를 확인한 뒤 후속으로 영상 요청
- 반복 작업에서 **이번 턴에 오버뷰까지 확인했던** 특정 변경이 안정화돼 정식 영상이 필요할 때

불확실하면 **먼저 물어본다** — "오버뷰 확인 먼저 하고, 통과하면 영상 뽑을까요?" 식으로.

### Overview 텍스트 직접 편집 (필수 기능)

모든 overview.html 상단 우측엔 **✎ Edit 버튼**이 있어야 한다. 기능은 독립 스킬로 분리됨 → **`hyperframes-overview-edit`** 스킬이 소스 오브 트루스. overview 를 새로 만들거나 수정할 때는 반드시 이 스킬의 3단계 스니펫(CSS·버튼·JS variant)을 포함시킨다.

**빠른 누락 체크**: `grep -L "class=\"edit-btn\"" topics/*/overview.html` — 출력된 파일은 기능 누락.

**사용 흐름**:
1. 브라우저에서 Edit 버튼 클릭 → 텍스트 요소들이 파란 점선으로 편집 가능 상태
2. 직접 타이핑해 수정
3. Done 클릭 → live 서버가 `index.html` + `overview.html` 에 변경사항을 즉시 반영 + 토스트 알림
4. static 서버로 열었거나 `/save` 실패 시에만 agent-readable 패치가 클립보드에 복사됨 → 사용자가 대화창에 붙여넣으면 agent 는 `hyperframes-overview-edit/references/patch-parser.md` 규칙에 따라 양쪽 파일에 반영

## SNS 카드뉴스 템플릿 규칙 — 4개만 허용

인스타그램/SNS 카드뉴스는 반드시 `hyperframes-card-news` 스킬을 사용한다. 이 스킬은 전체 카드뉴스 조립을 담당하고, 개별 카드 타입은 아래 4개 하위 스킬이 소스 오브 트루스다.

| 허용 템플릿 | 하위 스킬 | 용도 |
|---|---|---|
| `photo-cover` | `hyperframes-card-news-work-photo-cover` | 전면 사진형 오프닝/마감 |
| `video-cover` | `hyperframes-card-news-work-video-cover` | 짧은 무음 영상형 오프닝 |
| `stat` | `hyperframes-card-news-work-stat` | 큰 숫자·연도·비율 강조 |
| `image-feature` | `hyperframes-card-news-work-image-feature` | 이미지 중심 설명 카드 |

**규칙**:
- 카드뉴스의 `data-skill` 값은 `photo-cover`, `video-cover`, `stat`, `image-feature` 중 하나만 쓴다.
- `question`, `timeline`, `quote`, `closing`, `title-bullets` 같은 임의 카드 타입을 만들지 않는다.
- 새 카드뉴스를 만들거나 카드 타입을 수정할 때는 해당 `hyperframes-card-news-work-*` 하위 스킬을 함께 따른다.
- `video-cover`의 `<video>`는 카드 내부가 아니라 stage 직하위 timed media로 두고, overlay 카드는 별도 track에 둔다.
- `photo-cover`와 `video-cover`는 카피가 얹히는 영역을 충분히 어둡게 하고, 브랜드/출처 핸들은 검정 박스 위에 올린다.

## Default Font — Paperlogy

이 프로젝트의 **기본 웹폰트는 Paperlogy (페이퍼로지)**. 새로 만드는 모든 composition·카드뉴스·static.html에서 font-family 최우선으로 쓴다.

**왜 이걸 기본으로 잡아 두나**
- 무료 한국어 폰트 (SIL OFL, 상업 이용 자유)
- 한글 + 영문(Montserrat 계열) + 일문(M PLUS2) 한 폰트로 커버
- 9단계 weight (100 Thin ~ 900 Black) — 제목·본문 모두 대응
- **구글 폰트에 없다** → 프로젝트가 명시해 두지 않으면 agent가 기본값을 Inter / 시스템 sans로 잡는다

### 포함 방법

`<head>` 맨 위에:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/subsets/Paperlogy-dynamic-subset.css">
```

CSS font-family 스택:

```css
html, body {
  font-family: "Paperlogy", "Inter", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

**Weights (CSS numeric)**: 100 Thin / 200 ExtraLight / 300 Light / 400 Regular / 500 Medium / 600 SemiBold / 700 Bold / 800 ExtraBold / 900 Black

### 렌더 시 주의

hyperframes 렌더러는 **구글 폰트만 자동 캐시**한다. Paperlogy는 jsDelivr CDN에서 Puppeteer 브라우저가 직접 네트워크로 받아오므로:
- 온라인 환경: 정상 렌더
- 오프라인 / CI: Paperlogy 로드 실패 → 폴백 폰트(Inter 또는 시스템 sans)로 렌더

오프라인 결정성이 필수면 해당 토픽의 `assets/fonts/Paperlogy-*.woff2` 를 로컬 호스팅하고 `@font-face` 로 재선언한다:

```css
@font-face {
  font-family: "Paperlogy";
  src: url("assets/fonts/Paperlogy-4Regular.woff2") format("woff2");
  font-weight: 400;
  font-display: swap;
}
```

### 기존 토픽

이미 만들어진 토픽들(`topics/coffee-bean`, `topics/_instagram-demo` 등)은 Inter 기반으로 되어 있다. **새 토픽부터 Paperlogy 우선**, 기존 토픽은 개별 수정 시점에 순차 전환한다 — 렌더 결과물(파일명·색감·문단 줄바꿈)에 영향이 가므로 **일괄 마이그레이션은 금지**.

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
