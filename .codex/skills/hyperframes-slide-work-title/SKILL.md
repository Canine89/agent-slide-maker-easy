---
name: hyperframes-slide-work-title
description: >-
  HyperFrames 컴포지션의 title 슬라이드 전용 스킬. 큰 제목과 선택적 서브텍스트만으로
  구성되는 중앙 정렬 슬라이드를 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Title Slide (HyperFrames)

## 언제 쓰나

- 오프닝, 섹션 구분, 클로징처럼 제목 하나가 메시지의 전부일 때
- 이미지·불릿·태그 없이 타이포그래피만으로 임팩트를 줄 때
- 발표 흐름에서 "잠깐 멈춤"과 "주제 전환"을 알릴 때

## HTML 구조

```html
<div id="s-1" class="scene clip center"
     data-start="0" data-duration="6" data-track-index="0">
  <div class="eyebrow">카테고리 · 서브라벨</div>
  <div class="hero-title">메인 타이틀</div>
  <div class="hero-sub">보조 설명 (선택)</div>
</div>
```

## CSS 핵심

- `.scene.center` — `justify-content: center; align-items: center; text-align: center`
- `.eyebrow` — 24–32px, weight 500, letter-spacing 6–8px, uppercase, dim 색
- `.hero-title` — 280–340px, weight 800, letter-spacing 음수, 선택적 gradient text-clip
- `.hero-sub` — 36–42px, weight 400, dim 색
- 배경은 단색 또는 매우 옅은 radial gradient — 제목 자체가 주인공

## GSAP 엔트런스

```js
const start = 0; // data-start 값
tl.from("#s-1 .eyebrow",    { y: -20, opacity: 0, duration: 0.7, ease: "power3.out" }, start + 0.3);
tl.from("#s-1 .hero-title", { y: 80,  opacity: 0, duration: 1.1, ease: "expo.out"   }, start + 0.6);
tl.from("#s-1 .hero-sub",   {         opacity: 0, duration: 0.8, ease: "power2.out" }, start + 1.4);
```

- eases 최소 3종 섞기 (위 예시는 power3.out / expo.out / power2.out)
- t=0에서 바로 시작하지 말고 0.1–0.3s 오프셋

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [뱃지] 타이틀
서브텍스트 (선택)
```

헤딩 아래에 불릿(`-`), 태그(`>`), 이미지(`![]()`), evolution 마커(`<<`/`>>`) 없이 일반 텍스트만 있거나 비어 있으면 `title` 타입으로 감지한다.

## 작성 원칙

- 제목은 짧고 강하게 한 줄
- 서브텍스트는 1줄 이내 — 길어지면 `title-bullets`로 전환
- 불릿이 필요하면 이 타입이 아니라 `title-bullets`
- 화면 중앙에 제목만 크게 나오므로, 제목 자체가 충분히 의미를 전달해야 한다

## title vs title-bullets 구분

| 상황 | 타입 |
|------|------|
| 제목만, 또는 제목 + 짧은 서브텍스트 | `title` |
| 제목 + 설명 항목 나열 | `title-bullets` |

마크다운에 `-` 불릿이 하나라도 있으면 `title-bullets`로 감지한다.
