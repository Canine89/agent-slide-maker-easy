---
name: hyperframes-fx
description: >-
  HyperFrames 카드뉴스·슬라이드에 트랜지션·애니메이션·오버레이를 자동으로 매칭해
  배치하는 오케스트레이터. 사용자가 "카드뉴스에 효과 넣어줘", "트랜지션 적용",
  "fx 추가", "transition 뭐 쓸지 골라줘" 처럼 말할 때 진입점. 톤(brand/news/tech/
  minimalist/emotional)을 감지해 41개 fx sub-skill 중 적합한 조합을 고르고 설치·
  와이어링을 지시한다. 개별 효과 구현은 각 `hyperframes-fx-<slug>` 스킬로 위임.
---

# HyperFrames FX Orchestrator

## 언제 쓰나

- "카드뉴스에 효과 넣어줘", "transition 추가해줘", "fx 적용", "분위기 살리게 효과 추가" 같은 요청
- 이미 만든 카드·슬라이드 composition에 트랜지션·오버레이·UI 블록을 얹고 싶을 때
- 어떤 효과를 쓸지 판단이 필요한 모든 순간

개별 효과의 설치·HTML·파라미터를 이미 알고 있다면 해당 `hyperframes-fx-<slug>` sub-skill을 직접 호출하면 된다. 이 오케스트레이터는 **선택 로직**을 담는다.

## 흐름

### 1. 톤 감지

`references/tone-presets.md` 를 참조해 5가지 중 하나:

- **brand** — 브랜드·라이프스타일·커피·뷰티·여행
- **news** — 뉴스·사건·폭로·이슈
- **tech** — IT·데이터·AI·제품
- **minimalist** — 미니멀·에디토리얼·매거진
- **emotional** — 감성·회고·사연

감지 신호: 주제 이름, 기존 색 팔레트, 카드 내용 톤. 불명확하면 AskUserQuestion.

### 2. 카드 흐름 읽기

타겟 토픽 `index.html` 에서 각 `<div class="card clip ...">` 의 템플릿 타입(`photo-cover` / `question` / `stat` / `image-feature`)과 순서를 파악.

### 3. 레시피 매칭

`references/card-flow-recipes.md` 의 표에서 **톤 × 카드 흐름** 교차점에서 추천 조합을 가져온다. 일반적으로:

- 카드 간 트랜지션 2–3개 (카드 수 - 1)
- 지속형 오버레이 0–1개
- 카드별 액센트 0–2개

### 4. 설치

각 sub-skill의 설치 명령을 실행:

```bash
npx hyperframes add <slug1>
npx hyperframes add <slug2>
# ... 매칭된 효과 전부
```

자동으로 `topics/<주제>/compositions/` 또는 `compositions/components/` 에 파일 생성.

### 5. 와이어링

`index.html` 을 편집해 각 효과를 적절한 타이밍에 삽입. 구체적인 HTML 스니펫과 타이밍은 각 sub-skill의 "와이어링" 섹션 참조.

- **Shader transition / transition variant / UI block**: `<div data-composition-src="compositions/<file>.html" data-start="..." data-duration="..." data-track-index="1">`
- **Component overlay**: 각 컴포넌트의 HTML/CSS 스니펫을 카드 내부 또는 root 직하위에 삽입

### 6. 검증

```bash
npx hyperframes lint topics/<주제>
npx hyperframes render topics/<주제>
```

Lint 0 errors 확인 후 재렌더. 오버뷰는 정적이라 트랜지션이 보이지 않음 — **검증은 mp4 재생 기준**.

## 41개 Sub-skill 카탈로그

전체 목록은 `references/catalog.md` 참조. 카테고리 별 개수:

- **Shader Transitions**: 14개 (`hyperframes-fx-whip-pan`, `-flash-through-white`, `-chromatic-radial-split`, `-cinematic-zoom`, `-cross-warp-morph`, `-domain-warp-dissolve`, `-glitch`, `-gravitational-lens`, `-light-leak`, `-ridged-burn`, `-ripple-waves`, `-sdf-iris`, `-swirl-vortex`, `-thermal-distortion`)
- **Transition Variants**: 13개 (`hyperframes-fx-transitions-3d`, `-blur`, `-cover`, `-destruction`, `-dissolve`, `-distortion`, `-grid`, `-light`, `-mechanical`, `-other`, `-push`, `-radial`, `-scale`)
- **Component Overlays**: 3개 (`hyperframes-fx-grain-overlay`, `-grid-pixelate-wipe`, `-shimmer-sweep`)
- **UI Blocks**: 11개 (`hyperframes-fx-app-showcase`, `-data-chart`, `-flowchart`, `-instagram-follow`, `-logo-outro`, `-macos-notification`, `-reddit-post`, `-spotify-card`, `-tiktok-follow`, `-ui-3d-reveal`, `-x-post`, `-yt-lower-third`)

## 톤별 빠른 조합 (요약)

| 톤 | 추천 transition 트리오 | 오버레이 | 액센트 |
|----|------------------------|----------|--------|
| brand | whip-pan → sdf-iris → light-leak | grain-overlay (3–5%) | shimmer-sweep |
| news | flash-through-white → glitch → chromatic-radial-split | grain-overlay (5%) | 소셜 프루프 UI 블록 |
| tech | chromatic-radial-split → sdf-iris → cinematic-zoom | 없음 | data-chart / ui-3d-reveal |
| minimalist | cross-warp-morph → transitions-scale → domain-warp-dissolve | 없음 | 없음 |
| emotional | light-leak → ripple-waves → transitions-blur | grain-overlay (4%) | shimmer-sweep |

자세한 카드 흐름별 레시피 → `references/card-flow-recipes.md`
톤 매칭 원칙 → `references/tone-presets.md`

## 원칙

- **한 덱에 transition 종류 3개 이하** — 리듬 유지
- **지속형 오버레이는 하나만** — 노이즈 중첩 방지
- **타이밍 overlap 0.2–0.4초** — 하드컷 대신 자연스러운 연결
- **shader transition은 track-index 1** — 카드(track-index 0) 위에 얹기
- **의심 나면 물어보지 말고 brand 톤 default** — 가장 안전
