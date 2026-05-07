---
name: hyperframes-fx-shimmer-sweep
description: >-
  Shimmer Sweep — 텍스트나 요소 위를 빛이 쓸고 지나가는 지속형 컴포넌트.
  강조·프리미엄 느낌. 톤: brand, news, emotional. 트리거: shimmer, 반짝임, 빛 쓸기,
  highlight sweep, 강조 효과, AI 액센트, premium highlight.
---

# Shimmer Sweep

## 언제 쓰나
- question 카드의 `em` 강조어, stat 카드의 큰 숫자 위 1회성 반짝임
- AI·프리미엄·강조 요소 위에 얹어 시선 유도
- **톤**: brand, news, emotional
- **쓰임 규칙**: 1카드당 1회 — 남발하면 효과 약화

## 설치
```bash
npx hyperframes add shimmer-sweep
```
→ `compositions/components/shimmer-sweep.html` 생성.

## 와이어링 (컴포넌트 방식)

`components/shimmer-sweep.html` 의 CSS를 가져와 타겟 요소에 클래스 또는 스니펫 적용. CSS gradient mask 기반.

```html
<!-- 예: question 카드의 em 강조어에 적용 -->
<div class="q-text">정말 <em class="shimmer-sweep">그것</em>이 답일까?</div>
```

```css
/* shimmer-sweep 컴포넌트 CSS 포함 */
.shimmer-sweep {
  /* gradient mask animation */
}
```

GSAP 타임라인에서 등장 시점 제어:
```js
tl.fromTo(".shimmer-sweep",
  { "--shimmer-x": "-100%" },
  { "--shimmer-x": "100%", duration: 1.0, ease: "power2.out" },
  s + 1.5);
```

## 파라미터
- sweep 색·속도·너비는 CSS custom properties

## 짝
- 잘 맞음: `grain-overlay`, `light-leak` (시네마 느낌)
- 피해야: 한 카드에 여러 요소에 동시 적용 금지
