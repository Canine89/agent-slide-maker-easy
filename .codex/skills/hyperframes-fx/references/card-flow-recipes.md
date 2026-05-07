# Card Flow Recipes — 카드 흐름별 레시피

현재 카드뉴스 4개 템플릿 (`photo-cover` / `video-cover` / `stat` / `image-feature`)의 조합별로 추천 전환·액센트 레시피.

## 카드뉴스 4장: video-cover/photo-cover → stat → image-feature → CTA/정리

### brand 톤
| 전환 | 효과 |
|------|------|
| 01→02 video-cover/photo-cover → stat | `whip-pan` (0.5s) |
| 02→03 stat → image-feature | `sdf-iris` (0.6s) |
| 03→04 image-feature → CTA/정리 | `light-leak` (0.8s) |
| 지속형 전 카드 | `grain-overlay` (3–5% opacity) |
| hook-title 액센트 | `shimmer-sweep` (1회, 등장 1초 후) |

### news 톤
| 전환 | 효과 |
|------|------|
| 01→02 | `flash-through-white` (0.4s) |
| 02→03 | `glitch` (0.6s) |
| 03→04 | `chromatic-radial-split` (0.5s) |
| 지속형 | `grain-overlay` (5% opacity) |

### tech 톤
| 전환 | 효과 |
|------|------|
| 01→02 | `chromatic-radial-split` (0.5s) |
| 02→03 | `sdf-iris` (0.6s) |
| 03→04 | `cinematic-zoom` (0.7s) |
| 지속형 | 없음 — 깨끗하게 |

### emotional 톤
| 전환 | 효과 |
|------|------|
| 01→02 | `light-leak` (0.7s) |
| 02→03 | `ripple-waves` (0.6s) |
| 03→04 | `transitions-blur` (0.8s) |
| 지속형 | `grain-overlay` (4% opacity) |

### minimalist 톤
| 전환 | 효과 |
|------|------|
| 01→02 | `cross-warp-morph` (0.8s) |
| 02→03 | `transitions-scale` (0.6s) |
| 03→04 | `domain-warp-dissolve` (0.8s) |
| 지속형 | 없음 |

## 3-카드 짧은 구성 (video-cover/photo-cover → stat → image-feature)

2번의 전환만 필요. 각 톤에서 위 표의 01→02, 02→03 을 그대로 적용.

## 5+카드 구성

전환 종류는 **3가지로 제한**해서 리듬 유지. 같은 전환을 2회 재사용해도 OK (예: 01→02 whip-pan, 02→03 sdf-iris, 03→04 light-leak, 04→05 sdf-iris 재사용).

## 특수 마감 카드 (CTA / 로고)

마지막 카드 대신 `logo-outro` UI 블록을 사용하면 시네마틱 로고 리빌 + 글로우 + 태그라인 페이드가 자동 재생된다. brand 톤에 가장 적합.

## 트랜지션 타이밍 원칙

- 기본 duration: 0.4–0.8초
- 카드 끝 0.3초 전에 시작해 다음 카드 0.2초 걸치게 overlap
- track-index를 본 카드(0)보다 높은 값(1)으로 설정해 위에 얹기
- shader 트랜지션은 자체적으로 이전/이후 프레임을 샘플링하므로 timing을 정확히 맞춰야 자연스러움

## 와이어링 예시 (카드 1→2 사이 whip-pan 삽입)

```html
<!-- Card 1: data-start="0" data-duration="5" -->
<!-- Card 2: data-start="5" data-duration="5" -->

<!-- whip-pan 트랜지션: 카드 1 끝(4.7초)부터 카드 2 시작(5.2초)까지 overlap -->
<div data-composition-src="compositions/whip-pan.html"
     data-start="4.7" data-duration="0.5"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 지속형 오버레이 와이어링 (grain-overlay)

컴포넌트는 각 카드 내부 또는 root 직하위에 삽입. 전체 duration(20초) 동안 지속:

```html
<!-- root 직하위 -->
<div class="fx-grain-overlay"
     data-start="0" data-duration="20" data-track-index="2">
  <!-- grain-overlay 컴포넌트의 HTML 스니펫 -->
</div>
```

컴포넌트는 shader 트랜지션과 달리 `data-composition-src` 가 아닌 **HTML/CSS 스니펫을 직접 삽입**한다 (`npx hyperframes add <component>` 하면 `compositions/components/` 에 파일이 생성되고, 그 내용을 복사해 넣거나 해당 클래스를 적용).
