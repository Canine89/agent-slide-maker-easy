---
name: hyperframes-overview-edit
description: >-
  `hyperframes-overview`의 하위 필수 편집 모듈. 모든 overview.html 에 반드시
  포함해야 하는 Edit 버튼, contentEditable 텍스트 수정, live 저장, static 패치
  fallback 기능을 제공한다. 새 오버뷰 생성 시에는 상위 `hyperframes-overview`가
  이 모듈을 함께 적용한다. 단독 사용은 기존 overview의 Edit 기능 누락 보강,
  오버뷰 텍스트 수정, 사용자가 붙여넣은 `# Overview edits — ...` 패치 반영에
  한정한다.
---

# Overview Text Edit Module (필수 하위 모듈)

## 이 스킬의 역할

이 스킬은 `hyperframes-overview`의 하위 필수 모듈이다. HyperFrames overview.html 에는 **항상** 텍스트 인라인 편집 기능이 있어야 한다.

이 스킬은:

1. overview 생성·수정 시 기능을 빠짐없이 포함시키는 **체크리스트·스니펫 소스**
2. live 서버 저장 및 static fallback 패치를 agent가 파일에 반영하는 파서 규칙

두 용도 모두 관장한다.

## 언제 이 스킬을 쓰나

- 새 overview.html을 만들 때 → 상위 `hyperframes-overview`와 함께 **반드시 3가지 스니펫 삽입** (아래 절차)
- 기존 overview.html을 수정·리뷰할 때 → **먼저 기능 누락 여부 확인** (아래 검증)
- 사용자가 `# Overview edits — ...` 로 시작하는 패치를 붙여넣었을 때 → `references/patch-parser.md` 참조해 파일에 반영

## 누락 여부 빠른 검증

```bash
# 기능이 빠진 overview.html 파일 찾기
grep -L "class=\"edit-btn\"" topics/*/overview.html
```

출력된 파일은 Edit 기능이 빠져있음 → 이 스킬 스니펫으로 추가.

## 적용 3단계

### Step 1: CSS 삽입

`references/css.html` 내용을 **`.aim-toast .toast-sel { ... }` 규칙 직후** 에 붙여넣는다. (`</style>` 바로 직전이 아니라, 카드 스타일이 나오기 전. Aim feature 블록 뒤.)

### Step 2: Edit 버튼 추가

`.header-right` 안 `<button class="aim-btn">` 직전에 한 줄:

```html
<button class="edit-btn" id="nav-edit" aria-label="text edit">Edit</button>
```

### Step 3: JS 삽입 (variant 선택)

IIFE 마지막 `})()` 직전에 Text Edit mode 블록을 삽입한다. **overview의 카드/슬라이드 앵커 속성에 따라 2종 중 하나 선택**:

| Overview 유형 | 앵커 속성 | JS 스니펫 |
|---------------|-----------|-----------|
| 카드뉴스 (1080×1080·1080×1350) | `data-card` | `references/js-card.html` |
| 16:9 슬라이드 (1920×1080) | `data-slide` | `references/js-slide.html` |

두 variant는 쿼리 셀렉터 및 패치의 "Card" vs "Slide" 라벨만 다름. 코드 나머지는 동일.

## 서빙 모드: Live vs Static

두 가지 서빙 모드가 있다.

### 1. Live 모드 (권장) — `serve-live.sh`

POST `/save` 엔드포인트가 있는 Python 서버. Done 버튼 클릭 시 브라우저가 `fetch('/save', ...)` 로 패치를 서버에 POST → 서버가 `index.html` + `overview.html` 을 **파일에 즉시 반영**.

```bash
bash .codex/skills/hyperframes-overview-edit/serve-live.sh topics/<주제> <포트>
```

- 사용자가 대화창에 패치 붙여넣을 필요 없음
- 토스트: "✓ N건 반영됨 (파일 직접 수정) — 오른쪽 화면과 왼쪽 썸네일이 함께 갱신됨"
- agent 가 대화에 참여하지 않아도 편집이 저장됨 (단, 렌더는 여전히 사용자 승인 후)

### 2. Static 모드 (fallback) — `serve.sh`

기존 `hyperframes-overview/serve.sh` 는 POST 엔드포인트가 없음. 이 경우 브라우저는 fetch 실패 → 자동으로 **클립보드 복사 모드로 폴백**.

- 토스트: "✎ N개 변경 클립보드 복사됨 — 대화창에 붙여넣어 agent 반영 요청"
- 사용자가 대화에 패치 붙여넣음 → agent 가 `references/patch-parser.md` 따라 반영

> 브라우저 측 코드는 **항상 live 를 먼저 시도**하고 실패 시 clipboard 로 폴백. 두 모드 모두 투명하게 지원된다.

## 패치 포맷

사용자가 Done 버튼 클릭 시 클립보드에 아래 포맷이 복사되거나(static), live 서버의 `/save` 엔드포인트로 전송됨:

```
# Overview edits — <topic-id> (N change(s))

## Card 3 (question)
- .q-text
  OLD: 기존 텍스트 (innerHTML, 인라인 태그 포함 가능)
  NEW: 수정된 텍스트

## Card 5 (stat)
- .stat-label
  OLD: ...
  NEW: ...
```

16:9 slide variant는 `## Card N` 대신 `## Slide N` 헤더 사용.

## Agent 쪽 패치 반영 절차

사용자가 위 포맷의 마크다운을 대화창에 붙여넣으면, **agent는 `references/patch-parser.md`의 규칙에 따라** 파일에 반영한다. 요약:

1. 헤더 `# Overview edits — <topic>` 에서 topic 식별 → `topics/<topic>/` 로 경로 확정
2. 각 `## Card N (skill)` / `## Slide N (skill)` 섹션마다:
   - **index.html**: `<div id="c-N"` 또는 `<div id="s-N"` 블록 찾기 → 지정된 CSS 클래스 요소에서 OLD 를 NEW 로 Edit
   - **overview.html**: 같은 카드의 `[data-card="N"]` 또는 `[data-slide="N"]` 블록에서 동일 Edit
3. 두 파일 양쪽에 적용 후 사용자에게 요약 보고 ("N건 반영, 파일 2개 수정")
4. **렌더는 자동 실행하지 않음** — AGENTS.md의 overview-first 규칙에 따라 사용자 승인 기다림

## 한계·주의사항

- **텍스트 전용 leaf만 편집 가능** — IMG, `aria-hidden`, 블록 자식(div/ul/ol/section) 가진 요소는 잠금
- **인라인 태그 보존** — `<em>`, `<strong>`, `<br>`, `<span>` 등은 innerHTML 레벨에서 diff 되므로 편집 중에도 유지됨
- **세션 내 일시 저장** — 새로고침 전에 Done 클릭해 패치 복사할 것
- **썸네일 동기화** — Done 클릭 시 변경된 카드/슬라이드의 좌측 스트립 썸네일 clone을 오른쪽 최신 DOM에서 즉시 재생성한다. PDF/내보내기 전에 새로고침할 필요가 없게 유지해야 한다.
- **썸네일 렌더 일치** — 좌측 썸네일은 유지하되, 우측 편집 화면과 같은 display 모델을 써야 한다. 16:9 슬라이드는 `.thumb .scene { display: flex; }`, 카드뉴스는 `.thumb .card { display: flex; }` 를 명시한다. 이 규칙이 빠지면 같은 DOM clone이어도 flex 레이아웃이 달라져 썸네일과 편집 화면이 다르게 보인다.
- **PDF/내보내기 기준** — 브라우저 PDF/print/export 는 좌측 strip clone이 아니라 우측 `#detail-frame` 의 원본 카드/슬라이드를 기준으로 한다. overview 템플릿에는 `@media print` 로 `.strip`, `.main-header`, Aim/Edit UI를 숨기고 `.detail-frame` 내부 원본만 페이지 단위로 출력하는 CSS를 포함해야 한다.

## 통합 테스트

새로 만든 overview를 HTTP 서빙 후 브라우저에서:

- [ ] 우상단 Edit 버튼이 Aim 버튼 왼쪽에 보이는지
- [ ] 클릭 시 텍스트 요소들에 파란 점선 아웃라인이 뜨는지 (호버 시 진해지고, 포커스 시 실선)
- [ ] 한 단어 수정 후 Done 누르면 live 서버에서는 "✓ N건 반영됨", static 서버에서는 "✎ N개 변경 클립보드 복사됨" 토스트가 뜨는지
- [ ] Done 후 왼쪽 축소 썸네일이 오른쪽 편집 화면과 같은 레이아웃/텍스트로 즉시 갱신되는지
- [ ] PDF/print 결과가 왼쪽 strip 없이 원본 슬라이드/카드 페이지만 포함하는지
- [ ] static 서버 fallback에서 붙여넣기한 패치가 위 포맷과 정확히 일치하는지

6개 모두 통과해야 기능 OK.

## 관련 스킬

- `hyperframes-overview` — 16:9 슬라이드덱용 overview 생성기 (이 스킬과 짝)
- `hyperframes-card-news` — 카드뉴스 overview 생성기 (이 스킬과 짝)
- AGENTS.md — "Review Workflow — Overview First, Render Second" 섹션에 이 기능 사용법 문서화
