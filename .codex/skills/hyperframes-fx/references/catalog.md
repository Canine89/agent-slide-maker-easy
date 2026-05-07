# Catalog — 전체 효과 한 눈 리스트

41개 효과를 카테고리별로 정리. 각 항목 옆에 sub-skill 이름과 대표 톤 매칭.

## Shader Transitions (14) — 씬 간 GPU 트랜지션

| 효과 | Slug | 대표 톤 | 한 줄 |
|------|------|---------|-------|
| Whip Pan | `whip-pan` | brand, news | 빠른 카메라 휘젓기 |
| Flash Through White | `flash-through-white` | news | 흰빛 플래시 크로스페이드 |
| Chromatic Radial Split | `chromatic-radial-split` | tech, news | 색 분리 + 방사형 찢김 |
| Cinematic Zoom | `cinematic-zoom` | tech, brand | 드라마틱 줌 블러 |
| Cross Warp Morph | `cross-warp-morph` | minimalist | 교차 워프 모핑 |
| Domain Warp Dissolve | `domain-warp-dissolve` | minimalist, emotional | 프랙탈 노이즈 디졸브 |
| Glitch | `glitch` | news, tech | 디지털 글리치 아티팩트 |
| Gravitational Lens | `gravitational-lens` | tech | 중력 렌즈 왜곡 |
| Light Leak | `light-leak` | brand, emotional | 시네마틱 라이트 리크 |
| Ridged Burn | `ridged-burn` | news | 터뷸런스 태움 |
| Ripple Waves | `ripple-waves` | emotional | 동심원 물결 |
| SDF Iris | `sdf-iris` | brand, tech | SDF 홍채 리빌 |
| Swirl Vortex | `swirl-vortex` | news | 소용돌이 |
| Thermal Distortion | `thermal-distortion` | - | 열기 아지랑이 |

## Transition Variants (13) — 카테고리형 트랜지션 쇼케이스

| 효과 | Slug | 특징 |
|------|------|------|
| 3D | `transitions-3d` | 3D 플립·회전 |
| Blur | `transitions-blur` | 블러 기반 |
| Cover | `transitions-cover` | 덮기·벗기기 슬라이드 |
| Destruction | `transitions-destruction` | 파괴·깨짐 |
| Dissolve | `transitions-dissolve` | 디졸브·페이드 |
| Distortion | `transitions-distortion` | 왜곡 |
| Grid | `transitions-grid` | 그리드 타일 |
| Light | `transitions-light` | 글로우·플래시 |
| Mechanical | `transitions-mechanical` | 셔터·조리개 |
| Other | `transitions-other` | 기타 창의적 |
| Push | `transitions-push` | 밀어내기 슬라이드 |
| Radial | `transitions-radial` | 방사형 와이프 |
| Scale | `transitions-scale` | 스케일·줌 |

## Component Overlays (3) — 지속형 위 레이어

| 효과 | Slug | 쓰임 |
|------|------|------|
| Grain Overlay | `grain-overlay` | 필름 그레인 질감 |
| Grid Pixelate Wipe | `grid-pixelate-wipe` | 그리드 픽셀 디졸브 |
| Shimmer Sweep | `shimmer-sweep` | 텍스트 빛 쓸기 |

## UI Blocks (11) — 특정 UI 리빌·목업

| 효과 | Slug | 쓰임 |
|------|------|------|
| App Showcase | `app-showcase` | 3개 스마트폰 플로팅 제품쇼케이스 |
| Data Chart | `data-chart` | NYT 스타일 수치 스태거 리빌 |
| Flowchart | `flowchart` | SVG 커넥터 결정 트리 |
| Instagram Follow | `instagram-follow` | 인스타 팔로우 프로필 카드 |
| Logo Outro | `logo-outro` | 시네마틱 로고 리빌 + 태그라인 |
| macOS Notification | `macos-notification` | 맥OS 알림 목업 |
| Reddit Post | `reddit-post` | Reddit 포스트 카드 |
| Spotify Card | `spotify-card` | Spotify 플레이어 카드 |
| TikTok Follow | `tiktok-follow` | TikTok 팔로우 오버레이 |
| 3D UI Reveal | `ui-3d-reveal` | 퍼스펙티브 3D UI 등장 |
| X Post | `x-post` | X/트위터 포스트 카드 |
| YouTube Lower Third | `yt-lower-third` | 유튜브 구독 로워서드 |

## 참고

- 모든 효과는 `npx hyperframes add <slug>` 로 설치
- **shader transitions, transition variants, UI blocks** → `compositions/<slug>.html` 생성, `data-composition-src` 로 참조
- **component overlays** → `compositions/components/<slug>.html` 생성, HTML/CSS 스니펫 복사 방식
- 상세한 와이어링·파라미터는 각 sub-skill (`/hyperframes-fx-<slug>`) 참조
