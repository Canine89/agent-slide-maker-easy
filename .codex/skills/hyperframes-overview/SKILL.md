---
name: hyperframes-overview
description: >-
  HyperFrames 오버뷰 상위 스킬. 주제 폴더에 static `overview.html`을 만들고,
  좌측 썸네일 스트립 + 우측 디테일 프리뷰 + Aim 요소 선택기 + 필수 Edit 텍스트
  편집 모듈을 갖춘 정적 리뷰 페이지를 구성한다. `hyperframes-overview-edit`는
  이 스킬의 하위 필수 모듈로 함께 적용한다. 사용자가 "오버뷰 만들어줘",
  "overview.html 만들어줘", "정적 미리보기 만들자", "프리뷰 보여줘" 등으로
  요청할 때 사용.
---

# HyperFrames Overview

## 스킬 구조

이 스킬은 오버뷰 작업의 **상위 스킬**이다.

| 역할 | 스킬 |
|---|---|
| 오버뷰 생성·썸네일·디테일 프리뷰·Aim·서빙 흐름 | `hyperframes-overview` |
| Edit 버튼·contentEditable·live 저장·패치 파서 | `hyperframes-overview-edit` |

사용자는 보통 “오버뷰” 하나만 요청한다. agent는 `hyperframes-overview`를 먼저 적용하고, `hyperframes-overview-edit`를 필수 하위 모듈로 함께 적용한다.

`hyperframes-overview-edit`를 독립적으로 쓰는 경우는 기존 오버뷰의 Edit 기능 누락을 고치거나, 사용자가 `# Overview edits — ...` 패치를 붙여넣었을 때다.

## 언제 쓰나

- 한 topic 폴더에 15장 정도의 슬라이드가 있는 컴포지션을 정적으로 리뷰할 때
- 타임라인 애니메이션을 돌리지 않고 슬라이드 최종 상태만 넘겨가며 확인할 때
- 특정 요소를 콕 집어 수정 요청할 때 CSS 셀렉터를 빠르게 복사하고 싶을 때
- `npx hyperframes preview`의 스크럽 UI 대신 훨씬 가벼운 덱 뷰어가 필요할 때
- 사용자가 “프리뷰/미리보기”라고 말했지만 studio timeline 편집 의도가 분명하지 않을 때

> 16:9 슬라이드 타입 선택과 `data-skill` 허용 목록은 **`hyperframes-slide` 상위 스킬**이 담당한다. 이 스킬은 정적 리뷰 페이지 생성만 담당한다. overview를 만들거나 갱신할 때는 먼저 `hyperframes-slide`에서 슬라이드 타입을 확정하고, 여기서는 그 타입 값을 `data-slide`/`data-skill`로 반영한다.

## 무엇이 만들어지나

`topics/<주제>/overview.html` — 단일 파일, 프레임워크 런타임 불필요.

- **좌측 스트립**: 모든 슬라이드의 썸네일(16:9 비율 축소). 클릭하면 해당 슬라이드로 이동.
- **우측 디테일**: 현재 선택된 슬라이드를 1920×1080 → 뷰포트에 맞게 축소해서 보여줌.
- **네비**: `←/→`, `↑/↓`, `Space`, 숫자키(1–9, 0=10), 상단 버튼.
- **Aim 인스펙터**: 우상단 `Aim` 버튼 → 요소 호버 → 클릭 → `[data-slide="3"] > div.stat:nth-of-type(2) > div.num` 형태의 CSS 셀렉터가 클립보드로 복사됨.
- **Edit 텍스트 편집** (필수 하위 모듈): 우상단 `✎ Edit` 버튼 → contentEditable 로 직접 수정 → Done 누르면 live 서버에서는 `index.html` + `overview.html` 에 즉시 저장, static 서버에서는 agent-readable 패치를 클립보드로 복사. 자세한 구현·스니펫·파서 규칙은 **`hyperframes-overview-edit`** 스킬 참조. 16:9 기준은 `js-slide.html`, 카드뉴스 기준은 `js-card.html` variant 를 삽입한다.

> **필수 참조**: 이 스킬로 overview.html 을 만들거나 수정할 때는 **반드시 `hyperframes-overview-edit` 스킬**도 함께 적용해야 한다. CSS 블록·Edit 버튼·JS 블록이 빠지면 사용자가 텍스트를 수정할 수 없다. 누락 여부는 `grep -L "class=\"edit-btn\"" topics/*/overview.html` 로 한 번에 확인 가능.

## 썸네일·내보내기 필수 규칙

좌측 스트립 썸네일은 반드시 유지한다. 단, 썸네일은 별도 디자인이 아니라 우측 디테일 슬라이드 DOM을 축소한 미리보기여야 한다.

- 썸네일은 `scene.cloneNode(true)` 로 만들고, `.thumb .scene { display: flex; transform: scale(...); }` 를 명시한다. 우측 `.detail-frame .scene.active { display: flex; }` 와 같은 display 모델이어야 축소 썸네일과 편집 화면 레이아웃이 일치한다.
- 썸네일 라벨(`.thumb-label`)은 슬라이드 내용을 가리지 않게 기본 숨김, hover 때만 표시한다.
- Edit → Done 후에는 변경된 슬라이드 번호에 대해 `syncThumbFromScene(n)` 로 오른쪽 최신 DOM을 다시 clone 해서 좌측 썸네일을 즉시 갱신한다.
- PDF/print/export 는 좌측 strip 기준이 아니라 우측 `#detail-frame` 안의 원본 슬라이드 기준이어야 한다. `@media print` 에서 `.strip`, `.main-header`, Aim/Edit UI를 숨기고, `.detail-frame .scene` 전체를 1920×1080 페이지 단위로 출력한다.
- 이 규칙은 샘플 토픽뿐 아니라 새로 생성하는 모든 16:9 overview.html 에 적용한다.

## 파일 구조

```
.codex/skills/hyperframes-overview/
├── SKILL.md         (이 파일)
├── template.html    (재사용 가능한 베이스 템플릿)
└── serve.sh         (로컬 HTTP 서버 실행 스크립트 — CORS 회피용)
```

## 만드는 절차

### 1. 사전 조건 확인

- 해당 topic에 `index.html`이 있고, 각 씬이 `<div id="sN" class="scene clip ..." data-start="..." data-duration="..." data-track-index="...">` 구조여야 함.
- 이미 `overview.html`이 있다면 **확인 후 덮어쓰기**. 사용자가 수동 편집한 부분이 있는지 먼저 체크.

### 2. 템플릿 로드

[template.html](./template.html)을 읽는다. 이 템플릿에는 다음 placeholder 마커가 포함되어 있음:

| 마커 | 대체 내용 |
|------|-----------|
| `{{TOPIC_ID}}` | 예: `apple-history` |
| `{{TOPIC_BRAND}}` | 예: `Apple · 1976 — 2026` (각 슬라이드 하단에 표시) |
| `{{SLIDE_COUNT}}` | 예: `15` |
| `{{ACCENT_HEX}}` | UI 하이라이트 색 (topic의 `--accent`와 맞춤, 예: `#0A84FF`) |
| `{{ACCENT_RGB}}` | 같은 색의 RGB 값, shadow용 (예: `10, 132, 255`) |
| `{{SCENE_VARS}}` | topic `index.html`의 `:root { ... }` 블록 내용을 그대로 복사 |
| `{{SCENE_STYLES}}` | topic `index.html`의 씬 관련 CSS (`.scene`, `.eyebrow`, `.scene-title`, `.bullets`, `.stats`, `.flow`, `.quote-*` 등) 전체를 복사 |
| `{{SLIDES_HTML}}` | 각 씬을 변환한 HTML (아래 규칙 참조) |

### 3. 씬 변환 규칙 (index.html → overview.html)

각 씬 `<div id="sN" class="scene clip [center|quote]" data-start="..." ...>` 을 다음으로 바꾼다:

1. **`clip` 클래스 제거**, **timing attribute 제거** (`data-start`, `data-duration`, `data-track-index`, `data-media-start` 등).
2. **`id` 제거** — 셀렉터는 `[data-slide="N"]`로 앵커한다.
3. 대신 `data-slide="N"`과 `data-skill="<type>"` 추가. N은 1부터 시작.
4. 씬 안에 `brand`, `slide-num` 풋터 요소를 추가 (closing `</div>` 직전).
5. 씬 내부 요소에 `id` 참조(`#s1-b1` 등)가 있었다면 CSS 매칭용이 아니라 GSAP 타깃이었을 것 — 오버뷰에서는 애니메이션이 없으므로 **그대로 둬도 되지만** 셀렉터 단순화를 위해 제거 권장.

### 4. `data-skill` 분류

`data-skill` 값은 `hyperframes-slide` 상위 스킬의 하위 슬라이드 스킬 표를 따른다.

- 새 overview 생성 전: `hyperframes-slide`에서 각 슬라이드 타입을 먼저 확정한다.
- 기존 `index.html`에서 변환할 때: DOM 구조로 추정하되, 추정 결과가 애매하면 `hyperframes-slide`의 타입 선택 기준을 우선한다.
- 임의 타입을 만들지 않는다. 새 타입이 필요하면 먼저 `hyperframes-slide-work-<type>` 하위 스킬을 만들고 `hyperframes-slide` 표에 등록한다.

### 5. 풋터 요소

각 슬라이드의 마지막 자식으로 추가:

```html
<div class="brand">
  <span class="brand-dot"></span>
  <span class="brand-text">{{TOPIC_BRAND}}</span>
</div>
<div class="slide-num">
  <span class="skill">{{skill}}</span>N<span class="sep">/</span>{{SLIDE_COUNT}}
</div>
```

이 두 요소 스타일은 template의 공용 CSS에 이미 정의되어 있으므로 topic CSS에 없어도 된다.

### 6. 스타일 이식 시 주의

- topic `index.html`의 씬 CSS는 대부분 그대로 복사하되, **`body`나 `html` 셀렉터에 1920×1080 고정 크기를 적용하는 규칙은 제외** — overview에선 body가 뷰포트 전체고, 씬 크기는 `.scene { width: 1920px; height: 1080px }` 규칙에서만 설정돼야 한다.
- `.footer-brand` 같은 topic 고유 풋터 스타일이 있으면 제거 또는 `.brand`/`.slide-num` 템플릿 스타일로 대체.

### 7. 생성 후

- **이미지가 없는 덱**: 브라우저에서 `file:///...topics/<주제>/overview.html` 경로로 바로 열어도 동작.
- **이미지가 있는 덱**: 아래 "이미지 & CORS 대응" 절차를 따라 HTTP 서버로 서빙할 것.
- `npx hyperframes lint`는 overview.html을 검사하지 않으므로 별도 lint 불필요.

## 이미지 & CORS 대응

`file://`로 overview.html을 열면 브라우저가 이미지·폰트·캔버스 작업에 대해 보안 정책을 까다롭게 적용한다. 특히 Chrome은 로컬 파일 간 이미지 로드도 제한할 수 있고, canvas에 외부 이미지를 draw하면 "tainted canvas" 에러가 난다. **이미지를 포함한 오버뷰는 반드시 HTTP 컨텍스트에서 서빙**해야 한다.

### 이미지 삽입 시 지켜야 할 규칙

1. **경로는 topic 폴더 기준 상대경로로만** — `src="assets/hero.png"` ✓ / `src="/Users/..."` ✗ / `src="file:///..."` ✗
2. **외부 URL 이미지는 미리 로컬로 다운로드** — 원격 URL을 `<img>`에 직접 박지 말고 `assets/` 폴더에 받아놓은 뒤 상대경로로 참조:
   ```bash
   curl -o topics/<주제>/assets/hero.jpg https://example.com/hero.jpg
   ```
3. **Canvas 작업이 필요하면 `crossorigin="anonymous"`** — getImageData 등 픽셀 조작이 예정된 `<img>`에만 추가. 단순 표시용 `<img>`에는 불필요:
   ```html
   <img src="assets/hero.png" alt="..." crossorigin="anonymous" />
   ```
4. **Google Fonts는 이미 CORS-safe** — template.html의 `<link rel="preconnect" ... crossorigin>`이 처리.
5. **CSS `background-image` 도 동일 규칙** — 상대경로 사용, 외부 URL 지양.

### 로컬 HTTP 서버 실행 (권장)

이 스킬 폴더의 `serve.sh`를 사용한다. topic 경로를 넘기면 해당 폴더를 루트로 삼아 서버를 띄우고, 브라우저에서 `http://localhost:8765/overview.html`로 접근할 수 있다:

```bash
bash .codex/skills/hyperframes-overview/serve.sh topics/<주제>
# 또는 포트 지정
bash .codex/skills/hyperframes-overview/serve.sh topics/<주제> 9000
```

서버는 python3 → python → npx serve 순으로 fallback 한다. 터미널에서 `Ctrl+C`로 종료.

### 이미지 추가 체크리스트

사용자가 "여기 이미지 넣어줘" 라고 요청했을 때 다음 순서로 처리:

- [ ] 원본 파일을 `topics/<주제>/assets/` 에 배치 (외부 URL이면 `curl`로 다운로드)
- [ ] 해당 슬라이드의 `index.html`과 `overview.html` **양쪽**에 `<img src="assets/파일명" alt="설명" />` 삽입
- [ ] 슬라이드 레이아웃에 맞게 CSS 조정 (예: `.split-image img { width: 100%; height: 100%; object-fit: contain; }`)
- [ ] 기존 preview 서버가 꺼져 있다면 `serve.sh`로 HTTP 서버 기동 — `file://`로 열면 이미지가 깨질 수 있으므로 반드시 http://로 확인
- [ ] 사용자에게 `http://localhost:8765/overview.html` 경로 안내

## 원칙

- **한 파일 완결**: 외부 JS/CSS 없이 구글 폰트 CDN만 사용. 오프라인에서도 구조는 동작.
- **애니메이션 없음**: 모든 요소는 최종 상태로 렌더링. GSAP, `data-start`, `opacity: 0` 등 애니메이션 관련 속성 금지.
- **UI 크롬과 씬 스타일의 분리**: UI chrome은 `--ui-*` 변수로, 씬 스타일은 topic의 `--accent`/`--text` 등을 사용. 이름 충돌 없도록 확실히 구분.
- **셀렉터 앵커링**: 모든 셀렉터는 `[data-slide="N"]`로 시작해야 재현 가능. `id`나 nth-child에 의존하지 말 것.
- **재생성 가능**: 오버뷰를 다시 만들면 동일한 결과가 나와야 한다. 수동 커스터마이즈가 필요하다면 별도 파일에 분리.
