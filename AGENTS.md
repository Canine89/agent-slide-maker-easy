# HyperFrames 작업 라우팅 규칙

## Language

항상 한글로만 답한다.

## 이 문서의 역할

이 파일은 HyperFrames 자체 문법 설명서가 아니다. 이 저장소에서 반복되는 작업을 어떤 순서로 처리하고, 어떤 상위 스킬을 먼저 써야 하는지 정하는 라우팅 문서다.

세부 HTML/CSS/GSAP 구현 규칙은 각 스킬이 소스 오브 트루스다.

| 작업 | 사용할 스킬 |
|---|---|
| 16:9 발표/설명 슬라이드 | `hyperframes-slide` |
| 인스타그램/SNS 카드뉴스 | `hyperframes-card-news` |
| 정적 오버뷰 생성·서빙·편집 기능 포함 | `hyperframes-overview` |
| 오버뷰 패치 반영·Edit 기능 보강 | `hyperframes-overview-edit` (오버뷰 하위 모듈) |
| CLI/프레임워크 세부 문법 확인 | `hyperframes`, `hyperframes-cli` |

## Review Workflow — Overview First

이 프로젝트의 리뷰 흐름은 항상 **오버뷰 먼저, 영상 렌더는 그 다음**이다.

1. 슬라이드나 카드뉴스를 만들면 `topics/<주제>/overview.html`을 생성한다.
2. 오버뷰를 HTTP로 서빙해 사용자에게 URL을 먼저 제시한다.
3. 사용자가 내용을 검토하고 수정을 요청하면 반영한 뒤 오버뷰를 갱신한다.
4. 사용자가 오버뷰를 명시적으로 OK하고 영상을 요청한 뒤에만 `npx hyperframes render`를 실행한다.

사용자가 “프리뷰”, “preview”, “미리보기”라고 말해도 기본 의도는 정적 `overview.html` 확인으로 본다. HyperFrames studio preview는 “studio 열어줘”, “실시간 스크러빙으로 보고 싶어”처럼 live timeline 편집 의도가 분명할 때만 사용한다.

## Preview Port

HyperFrames studio preview가 필요할 때는 항상 포트 3000을 사용한다.

```bash
npx hyperframes preview --list
npx hyperframes preview --kill-all
lsof -nP -iTCP:3000 -sTCP:LISTEN
npx hyperframes preview topics/<주제-이름> --port 3000
```

주제를 바꿔 새 studio preview를 띄울 때도 먼저 `--kill-all`로 기존 서버를 정리한 뒤 3000에서 재시작한다.

## Overview 작업

오버뷰는 이 프로젝트의 기본 리뷰 화면이다. 슬라이드나 카드뉴스를 만든 뒤 바로 영상을 렌더하지 않고, 먼저 `topics/<주제>/overview.html`을 만들어 사용자가 정적으로 훑어보게 한다.

오버뷰 작업은 `hyperframes-overview` 상위 스킬을 사용한다. 이 스킬은 좌측 썸네일 스트립, 우측 디테일 프리뷰, Aim 선택기, HTTP 서빙 흐름을 담당한다.

`hyperframes-overview-edit`는 별도 작업 장르가 아니라 `hyperframes-overview`의 **필수 하위 편집 모듈**이다. 모든 `overview.html`에는 이 모듈의 Edit 기능이 들어가야 한다.

- 우상단 `Edit` 버튼 필수
- live 서버에서는 Done 클릭 시 `index.html`과 `overview.html`에 즉시 저장
- static fallback에서는 agent-readable 패치를 클립보드에 복사
- 누락 체크:

```bash
grep -L "class=\"edit-btn\"" topics/*/overview.html
```

기본 사용 순서:

1. `hyperframes-slide` 또는 `hyperframes-card-news`로 원본 `index.html`의 타입과 내용을 확정한다.
2. `hyperframes-overview`로 `overview.html`을 생성하거나 갱신한다.
3. `hyperframes-overview-edit` 모듈이 포함됐는지 확인한다.
4. live 서버로 오버뷰 URL을 제시한다.
5. 사용자가 오버뷰를 OK하고 영상 요청을 하면 그때 렌더한다.

오버뷰는 슬라이드/카드 타입을 결정하지 않는다. 16:9 슬라이드의 `data-skill` 결정은 `hyperframes-slide`, 카드뉴스의 `data-skill` 결정은 `hyperframes-card-news`를 따른다.

## 16:9 슬라이드 작업

1920×1080 발표/설명용 슬라이드는 반드시 `hyperframes-slide` 상위 스킬을 먼저 사용한다. 이 스킬은 덱 조립, 슬라이드 타입 선택, `data-skill` 관리, 오버뷰 동기화 흐름을 담당한다.

개별 슬라이드 구현은 하위 스킬이 소스 오브 트루스다.

| 허용 타입 | 하위 스킬 |
|---|---|
| `title` | `hyperframes-slide-work-title` |
| `title-bullets` | `hyperframes-slide-work-title-bullets` |
| `title-image` | `hyperframes-slide-work-title-image` |
| `title-tags` | `hyperframes-slide-work-title-tags` |
| `split` | `hyperframes-slide-work-split` |
| `stat` | `hyperframes-slide-work-stat` |
| `steps` | `hyperframes-slide-work-steps` |
| `compare` | `hyperframes-slide-work-compare` |
| `evolution-flow` | `hyperframes-slide-work-evolution-flow` |
| `quote` | `hyperframes-slide-work-quote` |
| `kindergarten-notice` | `hyperframes-slide-work-kindergarten-notice` |

규칙:
- 16:9 슬라이드의 `data-skill` 값은 위 허용 타입 중 하나만 쓴다.
- 새 슬라이드를 만들거나 타입을 수정할 때는 `hyperframes-slide`를 먼저 적용하고, 해당 하위 스킬을 함께 따른다.
- 슬라이드 작업 후 오버뷰가 필요하면 `hyperframes-overview`와 `hyperframes-overview-edit`를 함께 적용한다.
- 인스타그램/SNS 카드뉴스에는 이 규칙을 쓰지 않는다.

## SNS 카드뉴스 작업

인스타그램/SNS 카드뉴스는 반드시 `hyperframes-card-news` 상위 스킬을 먼저 사용한다. 이 스킬은 카드뉴스 조립, 카드 타입 선택, `data-skill` 관리, 오버뷰/렌더 흐름을 담당한다.

개별 카드 구현은 하위 스킬이 소스 오브 트루스다.

| 허용 템플릿 | 하위 스킬 |
|---|---|
| `photo-cover` | `hyperframes-card-news-work-photo-cover` |
| `video-cover` | `hyperframes-card-news-work-video-cover` |
| `stat` | `hyperframes-card-news-work-stat` |
| `image-feature` | `hyperframes-card-news-work-image-feature` |

규칙:
- 카드뉴스의 `data-skill` 값은 `photo-cover`, `video-cover`, `stat`, `image-feature` 중 하나만 쓴다.
- `question`, `timeline`, `quote`, `closing`, `title-bullets` 같은 임의 카드 타입을 만들지 않는다.
- 새 카드뉴스를 만들거나 카드 타입을 수정할 때는 `hyperframes-card-news`를 먼저 적용하고, 해당 하위 스킬을 함께 따른다.
- 16:9 발표 슬라이드에는 이 규칙을 쓰지 않는다.

## Typography

새로 만드는 composition, 카드뉴스, 오버뷰는 Paperlogy를 기본 웹폰트로 우선 사용한다.

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/subsets/Paperlogy-dynamic-subset.css">
```

```css
html, body {
  font-family: "Paperlogy", "Inter", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

기존 토픽은 개별 수정 시점에만 순차 전환한다. 렌더 결과의 줄바꿈과 색감에 영향이 있으므로 일괄 마이그레이션은 하지 않는다.

## Lint & Render

HTML composition을 생성하거나 수정한 뒤에는 토픽 경로를 지정해 lint를 실행한다.

```bash
npx hyperframes lint topics/<주제-이름>
```

오류는 반드시 수정한다. seek/visibility 관련 경고도 렌더 전에 해결한다.

렌더는 아래 중 하나일 때만 실행한다.

- 사용자가 “영상 만들어줘”, “render 해줘”, “mp4 뽑아줘”라고 명시적으로 요청
- 오버뷰 확인 후 후속으로 영상 요청
- 이번 턴에 오버뷰까지 확인한 변경이 안정화되어 사용자가 정식 영상 생성을 요구

불확실하면 먼저 “오버뷰 확인 후 영상 렌더까지 진행할까요?”라고 물어본다.
