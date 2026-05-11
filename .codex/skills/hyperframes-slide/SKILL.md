---
name: hyperframes-slide
description: >-
  HyperFrames 16:9 슬라이드덱 상위 스킬. 1920×1080 발표/설명용 슬라이드
  composition을 만들거나 수정할 때 먼저 사용한다. title, title-bullets,
  title-image, title-tags, split, stat, steps, compare, evolution-flow, quote,
  kindergarten-notice 같은 하위 `hyperframes-slide-work-*` 스킬을 알고 있고,
  슬라이드 타입 선택·data-skill 관리·index.html과 overview.html 동기화 흐름을
  총괄한다. 사용자가 "슬라이드 만들어줘", "16:9 덱", "발표 슬라이드",
  "overview에 슬라이드 추가", "slide work" 등을 요청할 때 사용.
---

# HyperFrames Slide Deck

## 역할

이 스킬은 1920×1080 HyperFrames 슬라이드덱의 **상위 조립 스킬**이다.

- 덱 전체 구조, 슬라이드 타입 선택, `data-skill` 값, 타임라인 흐름을 총괄한다.
- 개별 슬라이드의 HTML/CSS/GSAP 세부 구현은 하위 `hyperframes-slide-work-*` 스킬이 소스 오브 트루스다.
- `hyperframes-overview`는 정적 리뷰 페이지 생성기일 뿐이다. 슬라이드 타입과 레이아웃 판단은 이 스킬에서 먼저 결정한다.
- 인스타/SNS 카드뉴스는 이 스킬 대상이 아니다. 카드뉴스는 `hyperframes-card-news`를 사용한다.

## 하위 슬라이드 스킬 구조

슬라이드를 만들거나 수정할 때는 아래 표에서 타입을 고르고, 해당 하위 스킬을 함께 적용한다.

| `data-skill` | 하위 스킬 | 용도 |
|---|---|---|
| `title` | `hyperframes-slide-work-title` | 제목 + 선택적 서브텍스트만 있는 오프닝/섹션/클로징 |
| `title-bullets` | `hyperframes-slide-work-title-bullets` | 큰 제목 + 핵심 불릿 설명 |
| `title-image` | `hyperframes-slide-work-title-image` | 큰 제목 + 대표 이미지/스크린샷 |
| `title-tags` | `hyperframes-slide-work-title-tags` | 큰 제목 + 키워드 태그 묶음 |
| `split` | `hyperframes-slide-work-split` | 이미지/차트와 설명을 좌우 또는 상하 분할 |
| `stat` | `hyperframes-slide-work-stat` | 큰 숫자/KPI/지표 강조 |
| `steps` | `hyperframes-slide-work-steps` | 3단계 이상 순차 프로세스 |
| `compare` | `hyperframes-slide-work-compare` | 2~4개 항목 나란히 비교 |
| `evolution-flow` | `hyperframes-slide-work-evolution-flow` | 기존 상태 → 개선 상태, before/after 흐름 |
| `quote` | `hyperframes-slide-work-quote` | 핵심 문장/인용구를 크게 강조 |
| `kindergarten-notice` | `hyperframes-slide-work-kindergarten-notice` | 유치원·어린이집 학부모 안내/놀이 기록 스타일 |

임의 타입을 만들지 않는다. 새 타입이 필요하면 먼저 `hyperframes-slide-work-<type>` 하위 스킬을 만들고 이 표에 등록한다.

## 기본 캔버스와 공통 규칙

- 캔버스: `1920×1080`, 16:9.
- 루트: `<div id="root" data-composition-id="main" data-start="0" data-duration="..." data-width="1920" data-height="1080">`.
- 각 visible slide는 `class="scene clip"`을 포함하고 `data-start`, `data-duration`, `data-track-index`를 가진다.
- 슬라이드 duration 기본값은 6초. 읽을 양이 많으면 7~8초까지 늘린다.
- 기본 폰트는 Paperlogy 우선:
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/subsets/Paperlogy-dynamic-subset.css">
  ```
  ```css
  html, body { font-family: "Paperlogy", "Inter", "Helvetica Neue", Helvetica, Arial, sans-serif; }
  ```
- GSAP timeline은 반드시 paused로 만들고 `window.__timelines["main"]`에 등록한다.
- deterministic logic만 사용한다. `Date.now()`, `Math.random()`, runtime fetch 금지.

## 작업 순서

1. **요청 의도 분류**
   - 16:9 발표/설명 슬라이드면 이 스킬을 사용한다.
   - 인스타그램/SNS 카드뉴스면 `hyperframes-card-news`로 전환한다.
   - 오버뷰만 요청해도 슬라이드 타입 판단은 이 스킬 기준으로 한다.

2. **슬라이드 타입 선택**
   - 메시지 목적에 맞춰 위 표의 `data-skill` 중 하나를 고른다.
   - 선택한 타입의 하위 `hyperframes-slide-work-*` 스킬을 읽고 구조·CSS·GSAP 패턴을 따른다.

3. **`index.html` 수정**
   - 새 슬라이드는 `id="s-N"` 규칙을 쓴다.
   - `data-start`는 이전 슬라이드 종료 시각에 맞춘다.
   - 루트 `data-duration`을 전체 길이에 맞춰 갱신한다.
   - 하위 스킬의 GSAP 엔트런스 패턴을 timeline에 추가한다.

4. **`overview.html` 동기화**
   - 사용자가 오버뷰를 보고 있거나 슬라이드 내용을 리뷰해야 하면 `hyperframes-overview`와 `hyperframes-overview-edit`를 함께 사용한다.
   - 같은 슬라이드를 정적 DOM으로 추가하고 `data-slide="N"` + `data-skill="<type>"`를 붙인다.
   - 오버뷰의 총 슬라이드 수, 풋터 `N / total`, 좌측 썸네일 동기화 구조를 갱신한다.

5. **검증**
   - HTML composition을 수정했다면 `npx hyperframes lint topics/<주제>`를 실행한다.
   - 오류는 반드시 수정한다. 경고도 seek/visibility 관련이면 렌더 전에 해결한다.
   - 영상 렌더는 프로젝트 규칙상 사용자가 명시적으로 요청했을 때만 실행한다.

## 타입 선택 기준

- 제목 하나가 메시지의 전부다 → `title`
- 핵심 요점을 텍스트로 정리한다 → `title-bullets`
- 대표 이미지/스크린샷이 중심이다 → `title-image`
- 키워드 묶음으로 압축한다 → `title-tags`
- 시각 자료와 설명이 동시에 필요하다 → `split`
- 숫자 자체가 메시지다 → `stat`
- 3단계 이상 순서가 있다 → `steps`
- 여러 선택지나 항목을 나란히 비교한다 → `compare`
- 이전 상태와 이후 상태의 변화가 핵심이다 → `evolution-flow`
- 한 문장을 오래 남기고 싶다 → `quote`
- 어린이집/유치원 학부모 안내 톤이다 → `kindergarten-notice`

## `hyperframes-overview`와의 관계

`hyperframes-overview`는 다음만 담당한다.

- `index.html`의 슬라이드를 정적 리뷰용 `overview.html`로 변환
- 좌측 썸네일, 우측 디테일, Aim, Edit UI 제공
- live/static 서빙 흐름 제공

슬라이드 타입 표, 하위 스킬 선택, `data-skill` 허용 목록은 이 `hyperframes-slide` 스킬이 담당한다. overview를 만들거나 갱신할 때도 이 스킬의 타입 결정을 먼저 따른다.
