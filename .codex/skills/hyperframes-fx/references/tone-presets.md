# Tone Presets — 톤별 효과 조합표

5가지 톤에 대해 추천 효과 조합. `hyperframes-fx` 오케스트레이터가 사용자 주제와 문맥에서 톤을 감지한 뒤 이 표를 참조해 자동 매칭한다.

## brand — 브랜드·라이프스타일·커피·뷰티·여행

| 역할 | 추천 효과 (sub-skill) |
|------|------------------------|
| 카드 간 트랜지션 (에너지↑) | `hyperframes-fx-whip-pan` |
| 카드 간 트랜지션 (리빌)     | `hyperframes-fx-sdf-iris` |
| 카드 간 트랜지션 (호흡 완화) | `hyperframes-fx-light-leak` |
| 지속형 오버레이              | `hyperframes-fx-grain-overlay` |
| 텍스트 액센트                | `hyperframes-fx-shimmer-sweep` |
| CTA 카드 마감                | `hyperframes-fx-logo-outro` |

**피해야 할 조합**: glitch, chromatic-radial-split, thermal-distortion — 브랜드 감성에 과도한 디지털 노이즈.

## news — 뉴스·사건·폭로·이슈

| 역할 | 추천 효과 |
|------|-----------|
| 급정지 트랜지션 | `hyperframes-fx-flash-through-white` |
| 디지털 아티팩트 | `hyperframes-fx-glitch` |
| 카메라 휘젓기   | `hyperframes-fx-whip-pan` |
| 지속형 오버레이 | `hyperframes-fx-grain-overlay` |
| 인용·강조       | `hyperframes-fx-shimmer-sweep` |
| 소셜 프루프     | `hyperframes-fx-x-post` / `-reddit-post` / `-tiktok-follow` |

**피해야 할 조합**: light-leak, ripple-waves, thermal-distortion — 감성적이라 사건의 긴장감 약화.

## tech — IT·데이터·AI·제품

| 역할 | 추천 효과 |
|------|-----------|
| 색 분리 트랜지션 | `hyperframes-fx-chromatic-radial-split` |
| 홍채 리빌        | `hyperframes-fx-sdf-iris` |
| 줌 트랜지션      | `hyperframes-fx-cinematic-zoom` |
| 픽셀 와이프      | `hyperframes-fx-grid-pixelate-wipe` |
| 3D UI 등장       | `hyperframes-fx-ui-3d-reveal` |
| 제품 쇼케이스    | `hyperframes-fx-app-showcase` |
| 데이터 차트      | `hyperframes-fx-data-chart` |
| OS 알림 목업     | `hyperframes-fx-macos-notification` |
| 플로우차트       | `hyperframes-fx-flowchart` |

**피해야 할 조합**: grain-overlay, light-leak — 테크 감성엔 깨끗한 화면이 중요.

## minimalist — 미니멀·에디토리얼·매거진

| 역할 | 추천 효과 |
|------|-----------|
| 부드러운 디졸브 | `hyperframes-fx-domain-warp-dissolve` |
| 크로스 모프     | `hyperframes-fx-cross-warp-morph` |
| 스케일 트랜지션 | `hyperframes-fx-transitions-scale` |

**피해야 할 조합**: glitch, ridged-burn, swirl-vortex, destruction 계열 — 미니멀 톤과 충돌.

## emotional — 감성·사연·회고·자전적 스토리

| 역할 | 추천 효과 |
|------|-----------|
| 라이트 리크     | `hyperframes-fx-light-leak` |
| 블러 전환       | `hyperframes-fx-transitions-blur` |
| 파문 리빌       | `hyperframes-fx-ripple-waves` |
| 그레인 오버레이 | `hyperframes-fx-grain-overlay` |
| 시머 스윕       | `hyperframes-fx-shimmer-sweep` |

**피해야 할 조합**: glitch, chromatic-radial-split — 감성 톤에 방해.

## 톤 감지 힌트

오케스트레이터는 아래 신호로 톤 추정:

- **주제 이름**: `coffee-bean` / `brand-*` → brand, `news-*` / `issue-*` → news, `ai-*` / `tech-*` / `data-*` → tech, `editorial-*` → minimalist, `memoir-*` → emotional
- **기존 컴포지션 색감**: warm neutral(`#f2f0eb` 계열) → brand/emotional, cool neutral(`#0B0D10`) → news/tech
- **카드 내용**: 질문/감탄/느낌표 → news/emotional, 숫자 중심 → tech, 인용 중심 → emotional
- **불명확하면 사용자에게 AskUserQuestion으로 확인**
