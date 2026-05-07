---
name: hyperframes-slide-work-evolution-flow
description: >-
  HyperFrames 컴포지션의 evolution-flow 슬라이드 전용 스킬. 왼쪽 상태에서 오른쪽 상태로
  무엇이 어떻게 바뀌었는지를 2열 + 화살표 흐름으로 설명하는 슬라이드를 HTML + GSAP으로
  설계하거나 수정할 때 사용.
---

# Evolution Flow Slide (HyperFrames)

## 언제 쓰나

- 기존 상태와 개선 상태를 한 화면에서 대비할 때
- 입력 → 결과처럼 가운데 변화 축이 핵심일 때
- before/after 비교를 단순 나열이 아니라 인과 흐름으로 보여주고 싶을 때

## HTML 구조

```html
<div id="s-N" class="scene clip"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">개선</div>
  <div class="scene-title">검색 경험이 어떻게 바뀌었나</div>
  <div class="flow">
    <div class="flow-col" id="s-N-before">
      <div class="flow-label">기존</div>
      <div class="flow-heading">리스트 중심</div>
      <ul class="flow-list">
        <li>결과 목록이 길게 이어진다</li>
        <li>먼저 읽어야 할 답이 눈에 띄지 않는다</li>
      </ul>
    </div>
    <div class="flow-arrow" id="s-N-arrow">→</div>
    <div class="flow-col after" id="s-N-after">
      <div class="flow-label">개선</div>
      <div class="flow-heading">답 중심</div>
      <ul class="flow-list">
        <li>핵심 답이 먼저 보인다</li>
        <li>다음 클릭이 자연스럽게 이어진다</li>
      </ul>
    </div>
  </div>
</div>
```

## CSS 핵심

- `.flow` — `display: grid; grid-template-columns: 1fr 120px 1fr; gap: 40px; margin-top: 48–56px; flex: 1; max-height: 620px`
- `.flow-col` — 카드, `background: rgba(255,255,255,0.05); border: 1px solid rgba(...); border-radius: 24px; padding: 44px 40px; display: flex; flex-direction: column`
- `.flow-col.after` — 악센트 색 테두리/배경 그라디언트로 "도착 상태" 강조
- `.flow-label` — 배지 스타일 (24–28px, letter-spacing 3px, padding 8px 20px, border-radius 999px), `.flow-col.after .flow-label`은 accent 배경 + 대비 글자색
- `.flow-heading` — 44–56px, weight 700, line-height 1.2
- `.flow-list li` — 26–32px, weight 400, line-height 1.4, `padding-left: 28px`, `::before { content: "—" }`
- `.flow-arrow` — `display: flex; align-items: center; justify-content: center; font-size: 80px; font-weight: 200; color: accent`
- 이미지가 필요하면 `.flow-col` 안에 `.flow-image { aspect-ratio: 16/9 }` 추가

## GSAP 엔트런스

```js
const start = 39.2;
tl.from("#s-N .eyebrow",     { y: -15, opacity: 0, duration: 0.5, ease: "power3.out" }, start + 0.2);
tl.from("#s-N .scene-title", { y: 40,  opacity: 0, duration: 0.7, ease: "expo.out"   }, start + 0.4);
tl.from("#s-N-before", { x: -40, opacity: 0, duration: 0.7, ease: "power3.out" }, start + 0.9);
tl.from("#s-N-arrow",  { scale: 0.5, opacity: 0, duration: 0.5, ease: "back.out(1.7)" }, start + 1.3);
tl.from("#s-N-after",  { x: 40, opacity: 0, duration: 0.7, ease: "power3.out" }, start + 1.4);
```

- 왼쪽 패널이 먼저, 화살표, 오른쪽 패널 순으로 흐름이 읽히게
- 화살표는 `back.out`으로 튕기듯 등장해 리듬 차별화
- 요소 전체를 크게 흔들지 않고, 흐름의 방향이 읽히는 이동 + 순차 등장에 집중

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [개선] 검색 경험이 어떻게 바뀌었나

<< 기존 검색
- 결과 목록이 길게 이어진다
- 먼저 읽어야 할 답이 눈에 띄지 않는다

==

>> 개선된 검색
- 핵심 답이 먼저 보인다
- 다음 클릭이 자연스럽게 이어진다
```

- `<<` 로 시작하는 블록이 왼쪽 패널, `>>` 가 오른쪽 패널
- `==` 는 레이아웃 전환 신호일 뿐, 그 아래에는 내용을 쓰지 않는다
- 배지: `<< [기존] 타이틀` 형식으로 대괄호 안이 flow-label, 나머지가 flow-heading

이미지를 섞으려면 각 블록 안에 `![](...)`를 넣는다:

```markdown
<< 기존 가입
![](signup-before.png)
- 입력 단계가 길다

>> 개선된 가입
![](signup-after.png)
- 핵심 입력만 남았다
```

## 작성 원칙

- 왼쪽은 출발 상태, 오른쪽은 도착 상태만 적는다
- 좌우 불릿은 같은 개수로 맞출 필요는 없지만, 대응 관계가 느껴지게 쓴다
- 좌우 타이틀은 명사형보다 **상태형**이 더 읽기 좋다 ("리스트 중심" / "답 중심")
- 이미지가 있더라도 핵심 메시지는 불릿으로 다시 명시한다
- 변화 이유나 과정 설명이 필요하면 이 타입 안에 우겨 넣지 말고 다음 슬라이드로 분리

## 이미지가 없을 때

- `.flow-col` 안에 이미지 슬롯 생략 — 카드 자체가 충분한 시각 단위 역할
- 별도의 placeholder 컴포넌트는 필요 없음

## 비권장 상황

- 그냥 이미지 한 장과 설명 몇 줄이면 충분할 때 → `split` 또는 `title-image`
- 시간 순서가 4단계 이상으로 길게 이어질 때 → `steps`
- 3개 이상을 동시 비교할 때 → `compare`
