---
name: hyperframes-slide-work-title-bullets
description: >-
  HyperFrames 컴포지션의 title-bullets 슬라이드 전용 스킬. 큰 제목과 불릿 리스트 중심의
  설명 슬라이드를 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Title Bullets Slide (HyperFrames)

## 언제 쓰나

- 개념 설명, 요점 정리, 핵심 주장 전개의 가장 기본형
- 이미지 없이 메시지 자체를 전면에 세울 때

## HTML 구조

```html
<div id="s-N" class="scene clip"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">카테고리</div>
  <div class="scene-title">메인 타이틀</div>
  <ul class="bullets">
    <li id="s-N-b1"><strong>강조어</strong> — 설명 항목 1</li>
    <li id="s-N-b2">설명 항목 2</li>
    <li id="s-N-b3">설명 항목 3</li>
  </ul>
</div>
```

## CSS 핵심

- `.scene-title` — 88–120px, weight 800, letter-spacing 음수, 2줄 이내
- `.bullets` — `list-style: none; display: flex; flex-direction: column; gap: 24–28px`
- `.bullets li` — 38–44px, weight 400, line-height 1.45, `padding-left: 56px`, `word-break: keep-all`
- `.bullets li::before` — 좌측 라인 마커 (`content: ""; width: 32px; height: 2px; position: absolute`)
- `.bullets li strong` — 악센트 색 + weight 700

## GSAP 엔트런스

```js
const start = 5.6; // data-start
tl.from("#s-N .eyebrow",     { x: -20, opacity: 0, duration: 0.5, ease: "power3.out" }, start + 0.2);
tl.from("#s-N .scene-title", { y: 40,  opacity: 0, duration: 0.7, ease: "expo.out"   }, start + 0.4);
tl.from("#s-N-b1", { x: -20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 0.9);
tl.from("#s-N-b2", { x: -20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.05);
tl.from("#s-N-b3", { x: -20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.2);
```

- 불릿 간 stagger 0.12–0.15s
- 각 불릿에 id를 부여해 독립 제어 (또는 stagger 옵션으로 묶어도 됨)

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [뱃지] 타이틀

- 불릿 항목 1
- 불릿 항목 2
- 불릿 항목 3
```

## 작성 원칙

- 한 슬라이드에 불릿은 4개 이하
- 각 불릿은 한 문장으로 짧게
- 첫 불릿이 가장 중요한 메시지여야 한다
- 이미지가 필요해지면 `split` 또는 `title-image`로 전환

## 레이아웃 판단

- 기본은 1단 불릿 리스트
- 불릿 수가 많거나 3~4개 불릿이 모두 중간 길이 이상이면 2단 레이아웃(`grid-template-columns: 1fr 1fr`)로 전환 가능
- 2단 목적은 정보 증가가 아니라 **같은 밀도의 가독성 향상**
- 2단이어도 첫 불릿부터의 우선순위는 유지
- 너무 길어 2단으로도 해결 안 되면 슬라이드를 둘로 분리

## 2단 권장 / 비권장

| 상황 | 1단 / 2단 |
|---|---|
| 불릿 4개, 각 길이 비슷 | 2단 권장 |
| 3개이지만 각 2줄 이상 | 2단 권장 |
| 두 묶음을 병렬로 비교 | 2단 권장 |
| 불릿 2개 이하 | 1단 |
| 첫 불릿만 압도적으로 중요 | 1단 |
| 순차 흐름이라 위→아래로 읽어야 함 | 1단 |
