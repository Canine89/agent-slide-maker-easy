---
name: hyperframes-slide-work-stat
description: >-
  HyperFrames 컴포지션의 stat 슬라이드 전용 스킬. 큰 숫자와 짧은 설명으로 임팩트를 주는
  KPI/지표 슬라이드를 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Stat Slide (HyperFrames)

## 언제 쓰나

- 성과, KPI, 통계 수치를 강조할 때
- 숫자 자체가 메시지의 핵심일 때
- 1~3개 지표를 한 화면에 보여줄 때

## HTML 구조

```html
<div id="s-N" class="scene clip"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">카테고리</div>
  <div class="scene-title">메인 타이틀</div>
  <div class="stats">
    <div class="stat" id="s-N-st1">
      <div class="num">120만</div>
      <div class="label">월간 활성 사용자</div>
    </div>
    <div class="stat" id="s-N-st2">
      <div class="num">40%</div>
      <div class="label">운영 비용 절감</div>
    </div>
    <div class="stat" id="s-N-st3">
      <div class="num">3.2s</div>
      <div class="label">평균 응답 시간</div>
    </div>
  </div>
</div>
```

## CSS 핵심

- `.stats` — `display: grid; grid-template-columns: repeat(3, 1fr); gap: 48–64px; margin-top: 64px`
  - 지표 2개면 `repeat(2, 1fr)`, 1개면 가운데 정렬
- `.stat` — `border-top: 2px solid rgba(...); padding-top: 32px; display: flex; flex-direction: column`
- `.stat .num` — 110–140px, weight 800, line-height 1, letter-spacing 음수, 선택적 gradient text-clip
- `.stat .label` — 22–28px, weight 500, dim 색, line-height 1.4, `margin-top: 18–20px`
- 숫자는 `font-variant-numeric: tabular-nums`로 정렬감 강화

## GSAP 엔트런스

```js
const start = 22.4;
tl.from("#s-N .eyebrow",     { y: -15, opacity: 0, duration: 0.5, ease: "power3.out" }, start + 0.2);
tl.from("#s-N .scene-title", { y: 40,  opacity: 0, duration: 0.7, ease: "expo.out"   }, start + 0.4);
tl.from("#s-N-st1", { scale: 0.9, y: 30, opacity: 0, duration: 0.6, ease: "back.out(1.4)" }, start + 0.9);
tl.from("#s-N-st2", { scale: 0.9, y: 30, opacity: 0, duration: 0.6, ease: "back.out(1.4)" }, start + 1.1);
tl.from("#s-N-st3", { scale: 0.9, y: 30, opacity: 0, duration: 0.6, ease: "back.out(1.4)" }, start + 1.3);
```

- 숫자 자체가 카운트 업되어야 한다면 `gsap.to({ textContent: targetNumber, snap: { textContent: 1 } })` 패턴 추가 가능
- 단순 fade-in만으로도 충분한 경우가 많음 — 카운트 업은 결정적(deterministic)으로만

## 시각화 힌트 (선택)

숫자 옆에 `bar`/`ring` 보조 시각화가 필요하면 별도 DOM 요소로:

```html
<div class="stat-with-bar">
  <div class="num">120만</div>
  <div class="bar-track"><div class="bar-fill" style="width: 85%;"></div></div>
  <div class="label">월간 활성 사용자 · 목표 대비 85%</div>
</div>
```

- `bar` — 가로 프로그레스 바, GSAP `width: 0 → target%` 애니메이션
- `ring` — SVG `stroke-dasharray` 트윈으로 원형 게이지
- 없으면 숫자만으로도 충분

### 선택 기준

- `%` 값 → `ring` (퍼센트를 직관적으로 표현)
- 크기·양·속도 비교 → `bar`
- 단일 수치 강조 → 시각화 없이 숫자만

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [성과] 서비스 성장 지표

$ 120만
월간 활성 사용자

$ 40%
비용 절감률
```

- `$` 로 시작하는 줄이 숫자(value)
- 바로 다음 줄이 설명(label)
- 빈 줄로 지표 구분

시각화 힌트:

```markdown
$ 120만 [bar:85]
월간 활성 사용자

$ 40% [ring:40]
운영 비용 절감
```

## 작성 원칙

- 숫자는 짧고 임팩트 있게 (120만, 40%, 3.2s)
- 설명은 한 줄로 유지
- 1~3개가 적당 — 4개 이상이면 `split`이나 `title-bullets`로 전환
- 숫자에 단위 포함하면 더 읽기 쉬움
