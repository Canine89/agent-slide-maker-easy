---
name: hyperframes-slide-work-quote
description: >-
  HyperFrames 컴포지션의 quote 슬라이드 전용 스킬. 핵심 문장이나 인용구를 큰따옴표 장식과 함께
  크게 보여주는 중앙 정렬 슬라이드를 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Quote Slide (HyperFrames)

## 언제 쓰나

- 핵심 메시지를 강하게 남기고 싶을 때
- 인용구, 명언, 사용자 피드백을 보여줄 때
- 발표 흐름에서 잠깐 멈추고 리듬감을 줄 때

## HTML 구조

```html
<div id="s-N" class="scene clip quote"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">카테고리 · 인사이트</div>
  <div class="quote-mark">"</div>
  <div class="quote-body">좋은 디자인은 <em>가능한 적게</em> 디자인하는 것이다</div>
  <div class="quote-attrib">— Dieter Rams</div>
</div>
```

## CSS 핵심

- `.scene.quote` — `justify-content: center; align-items: center; text-align: center`
- `.quote-mark` — 200–240px, weight 900, accent 색, `opacity: 0.35`, `line-height: 0.7`
- `.quote-body` — 72–96px, weight 600–700, line-height 1.35, max-width 1500px, `word-break: keep-all`
- `.quote-body em` — `font-style: normal`, gradient text-clip 또는 accent 색
- `.quote-attrib` — 28–36px, weight 500, dim 색, letter-spacing 2–4px, `margin-top: 40–48px`

## GSAP 엔트런스

```js
const start = 33.6;
tl.from("#s-N .eyebrow",      { opacity: 0, duration: 0.6, ease: "power2.out" }, start + 0.2);
tl.from("#s-N .quote-mark",   { scale: 0.3, opacity: 0, duration: 0.8, ease: "back.out(1.8)" }, start + 0.5);
tl.from("#s-N .quote-body",   { y: 40, opacity: 0, duration: 1.0, ease: "expo.out" }, start + 0.9);
tl.from("#s-N .quote-attrib", { opacity: 0, duration: 0.7, ease: "power2.out" }, start + 1.8);
```

- 따옴표는 back.out 으로 등장해 리듬 차별화
- 본문은 아래에서 길게 올라오도록 expo.out

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [인사이트] 핵심 메시지

"" 좋은 디자인은 가능한 적게 디자인하는 것이다
— Dieter Rams
```

- `""` 로 시작하는 줄이 인용 문장
- `—` 또는 `--` 로 시작하는 줄이 출처 (선택)

## 작성 원칙

- 인용 문장은 1~2줄로 유지
- 출처가 없어도 됨 (자기 메시지 강조용)
- 불릿이나 태그를 섞지 않는다 — 인용문 자체에 집중
- 긴 문장이면 핵심만 발췌한다

## 클로징 슬라이드로 쓸 때

- 컴포지션의 마지막 씬이면 fade-out 허용 (전체 컴포지션의 유일한 예외)
- 중간 씬이면 exit 애니메이션 금지 — 다음 씬과의 오버랩이 트랜지션 역할
