---
name: hyperframes-slide-work-steps
description: >-
  HyperFrames 컴포지션의 steps 슬라이드 전용 스킬. 번호가 매겨진 순차 프로세스를 연결선과 함께
  보여주는 슬라이드를 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Steps Slide (HyperFrames)

## 언제 쓰나

- 순서가 있는 프로세스를 보여줄 때
- 워크플로우, 파이프라인, 절차를 설명할 때
- `evolution-flow`와 달리 3개 이상 단계가 필요할 때

## HTML 구조

```html
<div id="s-N" class="scene clip"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">프로세스</div>
  <div class="scene-title">배포 파이프라인</div>
  <ol class="steps">
    <li class="step" id="s-N-step1">
      <div class="step-num">1</div>
      <div class="step-body">코드 커밋</div>
    </li>
    <li class="step" id="s-N-step2">
      <div class="step-num">2</div>
      <div class="step-body">CI 테스트 실행</div>
    </li>
    <li class="step" id="s-N-step3">
      <div class="step-num">3</div>
      <div class="step-body">스테이징 배포</div>
    </li>
    <li class="step" id="s-N-step4">
      <div class="step-num">4</div>
      <div class="step-body">프로덕션 릴리즈</div>
    </li>
  </ol>
</div>
```

## CSS 핵심

- `.steps` — `list-style: none; display: flex; flex-direction: column; gap: 28px; margin-top: 56px; position: relative`
- `.step` — `display: flex; align-items: center; gap: 32px`
- `.step-num` — 원형 마커, `width: 72px; height: 72px; border-radius: 50%; background: accent; color: bg; display: flex; align-items: center; justify-content: center; font-size: 36px; font-weight: 800; flex-shrink: 0`
- `.step-body` — 38–44px, weight 500, line-height 1.4
- 연결선 — `.steps::before` 로 좌측 세로 라인 (`content: ""; position: absolute; left: 36px; top: 36px; bottom: 36px; width: 2px; background: rgba(...)`)

## GSAP 엔트런스

```js
const start = 28.0;
tl.from("#s-N .eyebrow",     { y: -15, opacity: 0, duration: 0.5, ease: "power3.out" }, start + 0.2);
tl.from("#s-N .scene-title", { y: 40,  opacity: 0, duration: 0.7, ease: "expo.out"   }, start + 0.4);
tl.from("#s-N-step1 .step-num",  { scale: 0, opacity: 0, duration: 0.5, ease: "back.out(1.7)" }, start + 0.9);
tl.from("#s-N-step1 .step-body", { x: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.0);
tl.from("#s-N-step2 .step-num",  { scale: 0, opacity: 0, duration: 0.5, ease: "back.out(1.7)" }, start + 1.2);
tl.from("#s-N-step2 .step-body", { x: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.3);
tl.from("#s-N-step3 .step-num",  { scale: 0, opacity: 0, duration: 0.5, ease: "back.out(1.7)" }, start + 1.5);
tl.from("#s-N-step3 .step-body", { x: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.6);
tl.from("#s-N-step4 .step-num",  { scale: 0, opacity: 0, duration: 0.5, ease: "back.out(1.7)" }, start + 1.8);
tl.from("#s-N-step4 .step-body", { x: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, start + 1.9);
```

- 번호 원은 `back.out` 으로 튕기듯 등장, 본문은 옆에서 들어오는 교차 리듬
- 연결선도 `scaleY: 0 → 1; transformOrigin: top`으로 흘러내리듯 그릴 수 있음

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [프로세스] 배포 파이프라인

1. 코드 커밋
2. CI 테스트 실행
3. 스테이징 배포
4. 프로덕션 릴리즈
```

- `1.` `2.` 같은 번호 리스트로 감지
- `-` 불릿(`title-bullets`)과 구분됨

## steps vs title-bullets vs evolution-flow

| 상황 | 타입 |
|------|------|
| 순서가 중요한 단계별 흐름 | `steps` |
| 순서 없는 나열 | `title-bullets` |
| 2개 상태 비교 (before/after) | `evolution-flow` |

## 작성 원칙

- 3~5단계가 적당
- 각 단계는 한 줄로 짧게
- 순서가 중요하지 않으면 `title-bullets`
- 번호 원형 마커 + 세로 연결선이 기본 레이아웃
