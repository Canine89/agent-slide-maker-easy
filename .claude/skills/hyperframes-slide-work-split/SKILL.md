---
name: hyperframes-slide-work-split
description: >-
  HyperFrames 컴포지션의 split 슬라이드 전용 스킬. 이미지와 불릿 설명을 좌우 또는 상하로
  분할 구성하는 슬라이드를 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Split Slide (HyperFrames)

## 언제 쓰나

- 스크린샷, 차트, 다이어그램을 설명할 때
- 시각 자료와 해설을 동시에 보여줘야 할 때

## HTML 구조 (가로형 · 좌우 분할)

```html
<div id="s-N" class="scene clip split"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">카테고리</div>
  <div class="scene-title">메인 타이틀</div>
  <div class="split-grid">
    <div class="split-image">
      <img src="assets/03-chart.png" alt="설명" crossorigin="anonymous" />
    </div>
    <ul class="bullets">
      <li id="s-N-b1">설명 항목 1</li>
      <li id="s-N-b2">설명 항목 2</li>
      <li id="s-N-b3">설명 항목 3</li>
    </ul>
  </div>
</div>
```

## HTML 구조 (세로형 · 상하 분할, 9:16 쇼츠)

```html
<div class="split-grid vertical">
  <div class="split-image">...</div>
  <ul class="bullets">...</ul>
</div>
```

## CSS 핵심

- `.split-grid` — `display: grid; grid-template-columns: 1fr 1fr; gap: 48–64px; margin-top: 48px; flex: 1`
- `.split-grid.vertical` — `grid-template-columns: 1fr; grid-template-rows: 1fr 1fr`
- `.split-image` — 컨테이너, 이미지 없을 때 dashed border + 옅은 배경으로 placeholder 역할
- `.split-image img` — `width: 100%; height: 100%; object-fit: contain`
- 불릿 쪽은 `title-bullets`의 `.bullets` 스타일 그대로 재사용

## GSAP 엔트런스

```js
const start = 22.4;
tl.from("#s-N .eyebrow",     { y: -15, opacity: 0, duration: 0.5, ease: "power3.out" }, start + 0.2);
tl.from("#s-N .scene-title", { y: 40,  opacity: 0, duration: 0.7, ease: "expo.out"   }, start + 0.4);
tl.from("#s-N .split-image", { x: -40, opacity: 0, duration: 0.7, ease: "power3.out" }, start + 0.9);
tl.from("#s-N-b1", { x: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.1);
tl.from("#s-N-b2", { x: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.25);
tl.from("#s-N-b3", { x: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.4);
```

- 이미지는 왼쪽에서, 불릿은 오른쪽에서 들어오는 방향성 일치

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [뱃지] 타이틀

![](03-chart.png)

- 설명 항목 1
- 설명 항목 2
```

이미지와 불릿이 동시에 있으면 `split` 타입.

## 작성 원칙

- 이미지는 **읽어야 할 대상**, 불릿은 **해석**을 제공해야 한다
- 불릿이 이미지를 반복 설명하지 않도록 쓴다
- 이미지가 없으면 `split`이 아니라 `title-bullets` 또는 `title-image`로 바꾼다
- 가로형은 좌우, 세로형(9:16 쇼츠)은 상하 분할이 기본

## 이미지가 없을 때

- `.split-image`에 dashed border + 옅은 반투명 배경을 두어 placeholder 역할 수행
- 실제 이미지 준비되면 `<img>`만 채워 넣으면 됨
