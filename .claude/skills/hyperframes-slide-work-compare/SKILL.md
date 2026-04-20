---
name: hyperframes-slide-work-compare
description: >-
  HyperFrames 컴포지션의 compare 슬라이드 전용 스킬. 2~4개 항목을 나란히 비교하는
  슬라이드를 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Compare Slide (HyperFrames)

## 언제 쓰나

- 2~4개 항목을 동시에 비교할 때
- 선택지, 옵션, 대안을 나란히 보여줄 때
- 각 항목의 특징을 불릿으로 설명할 때

## HTML 구조

```html
<div id="s-N" class="scene clip"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">비교</div>
  <div class="scene-title">프레임워크 선택</div>
  <div class="compare-grid">
    <div class="compare-col" id="s-N-c1">
      <div class="compare-heading">React</div>
      <ul class="compare-list">
        <li>생태계가 크다</li>
        <li>자유도가 높다</li>
      </ul>
    </div>
    <div class="compare-col" id="s-N-c2">
      <div class="compare-heading">Vue</div>
      <ul class="compare-list">
        <li>학습 곡선이 낮다</li>
        <li>공식 도구가 잘 갖춰져 있다</li>
      </ul>
    </div>
    <div class="compare-col" id="s-N-c3">
      <div class="compare-heading">Svelte</div>
      <ul class="compare-list">
        <li>번들 크기가 작다</li>
        <li>컴파일 타임 최적화</li>
      </ul>
    </div>
  </div>
</div>
```

## CSS 핵심

- `.compare-grid` — `display: grid; gap: 32–40px; margin-top: 48px; flex: 1`
  - 2열: `grid-template-columns: 1fr 1fr`
  - 3열: `repeat(3, 1fr)` (기본)
  - 4열: `repeat(4, 1fr)`
- `.compare-col` — 카드 스타일, `background: rgba(255,255,255,0.05); border: 1px solid rgba(...); border-radius: 20px; padding: 36–40px`
- `.compare-heading` — 44–56px, weight 700, `border-bottom: 2px solid accent; padding-bottom: 16px; margin-bottom: 20px`
- `.compare-list li` — 26–32px, weight 400, line-height 1.4, `padding-left: 28px`, marker는 `—` 또는 점

## GSAP 엔트런스

```js
const start = 33.6;
tl.from("#s-N .eyebrow",     { y: -15, opacity: 0, duration: 0.5, ease: "power3.out" }, start + 0.2);
tl.from("#s-N .scene-title", { y: 40,  opacity: 0, duration: 0.7, ease: "expo.out"   }, start + 0.4);
tl.from("#s-N-c1", { y: 60, opacity: 0, duration: 0.6, ease: "power3.out" }, start + 0.9);
tl.from("#s-N-c2", { y: 60, opacity: 0, duration: 0.6, ease: "power3.out" }, start + 1.05);
tl.from("#s-N-c3", { y: 60, opacity: 0, duration: 0.6, ease: "power3.out" }, start + 1.2);
```

- 컬럼은 동일 방향(아래 → 위) 스태거로 일관성 강조
- 컬럼 간 간격 0.12–0.18s

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [비교] 프레임워크 선택

|| React
- 생태계가 크다
- 자유도가 높다

|| Vue
- 학습 곡선이 낮다
- 공식 도구가 잘 갖춰져 있다

|| Svelte
- 번들 크기가 작다
- 컴파일 타임 최적화
```

- `||` 로 시작하는 줄이 컬럼 제목
- 그 아래 `-` 불릿이 해당 컬럼의 설명

## compare vs evolution-flow 구분

| 상황 | 타입 |
|------|------|
| A에서 B로 변한 흐름 (방향성 있음) | `evolution-flow` |
| A, B, C를 동시에 비교 (대등 관계) | `compare` |

## 작성 원칙

- 2~4개 컬럼이 적당
- 컬럼 제목은 짧게 (1~2 단어)
- 각 컬럼의 불릿 수를 비슷하게 맞추면 균형이 좋다
- 5개 이상 컬럼은 가독성이 떨어지므로 분리
