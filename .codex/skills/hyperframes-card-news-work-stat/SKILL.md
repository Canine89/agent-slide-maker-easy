---
name: hyperframes-card-news-work-stat
description: >-
  HyperFrames 인스타 카드뉴스의 stat 카드 전용 작업 스킬. 큰 숫자 하나,
  짧은 라벨, 한 줄 설명으로 KPI·연도·수량·비율을 강조하는 카드 작업에 사용.
  hyperframes-card-news의 4개 허용 템플릿 중 stat의 소스 오브 트루스.
---

# Card News Work: Stat

## 역할

`stat`은 숫자 하나로 메시지를 만드는 카드다. 연도, 수량, 비율, 순위, 기간처럼 숫자가 중심일 때만 사용한다.

허용 클래스:

```html
<div id="c-N" class="card clip stat-card"
     data-start="..." data-duration="5" data-track-index="0">
```

## 구조

```html
<div id="c-N" class="card clip stat-card"
     data-start="10" data-duration="5" data-track-index="0">
  <div class="eyebrow">By the Numbers</div>
  <div class="stat-num">1,000<span class="stat-unit">+</span></div>
  <div class="stat-label">핵심 지표 라벨</div>
  <div class="stat-desc">지표를 설명하는 한 줄. 출처·기간이 필요하면 여기에 넣는다.</div>
  <div class="page-indicator">03 · 08</div>
</div>
```

## 내용 규칙

- 한 카드에는 숫자 하나만 둔다.
- `stat-num`은 최대 8자 안팎을 권장한다. 길면 단위를 `stat-unit`으로 분리한다.
- `stat-label`은 한 메시지, 1-2줄.
- `stat-desc`는 보조 맥락, 1-2문장.
- 숫자가 중심이 아닌 연대기 설명은 `image-feature`로 보내거나 문장을 숫자 중심으로 다시 쓴다.

## CSS 규칙

```css
.card.stat-card {
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 96px 72px;
}
.stat-num {
  font-size: 160px;
  font-weight: 820;
  line-height: 0.95;
  letter-spacing: -0.04em;
  font-variant-numeric: tabular-nums;
}
.stat-unit {
  font-size: 58px;
  font-weight: 620;
}
.stat-label {
  margin-top: 38px;
  font-size: 56-64px;
  font-weight: 760-820;
  line-height: 1.08;
  letter-spacing: -0.019em;
}
.stat-desc {
  margin-top: 24px;
  font-size: 28-32px;
  line-height: 1.38-1.45;
}
```

## 변형

- light: `background: #f5f5f7`, text `#1d1d1f`.
- dark: `class="card clip stat-card dark"` 가능. 단, `data-skill`은 여전히 `stat`.
- 브랜드 스타일에서 CTA blue는 숫자 강조보다 버튼/링크에 아껴 쓴다. 숫자 단위 정도에만 제한적으로 사용한다.

## GSAP

```js
tl.from("#c-N .eyebrow", { y: -15, opacity: 0, duration: 0.5, ease: "power3.out" }, s + 0.2);
tl.from("#c-N .stat-num", { scale: 0.88, opacity: 0, duration: 0.8, ease: "back.out(1.4)" }, s + 0.5);
tl.from("#c-N .stat-label", { y: 22, opacity: 0, duration: 0.65, ease: "power2.out" }, s + 1.1);
tl.from("#c-N .stat-desc", { y: 16, opacity: 0, duration: 0.55, ease: "power2.out" }, s + 1.5);
tl.from("#c-N .page-indicator", { opacity: 0, duration: 0.4, ease: "power2.out" }, s + 2.0);
```

## 체크

- [ ] `data-skill="stat"`로 overview에 기록
- [ ] 숫자 하나만 강조
- [ ] 설명은 숫자를 보조함
- [ ] 긴 문단·불릿 리스트로 변질되지 않음
