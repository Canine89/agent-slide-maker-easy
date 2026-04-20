---
name: hyperframes-slide-work-title-tags
description: >-
  HyperFrames 컴포지션의 title-tags 슬라이드 전용 스킬. 큰 제목과 키워드 태그 묶음을
  중심으로 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Title Tags Slide (HyperFrames)

## 언제 쓰나

- 개념을 짧은 키워드로 압축해 보여줄 때
- 기술 스택, 핵심 속성, 비교 축, 요약 인덱스

## HTML 구조

```html
<div id="s-N" class="scene clip"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">카테고리</div>
  <div class="scene-title">메인 타이틀</div>
  <div class="scene-subtitle">보조 설명 (선택)</div>
  <div class="tags">
    <div class="tag">태그1</div>
    <div class="tag">태그2</div>
    <div class="tag accent">강조태그</div>
    <div class="tag">태그4</div>
    <div class="tag">태그5</div>
  </div>
</div>
```

## CSS 핵심

- `.tags` — `display: flex; flex-wrap: wrap; gap: 20–24px; margin-top: 56px`
- `.tag` — `padding: 18–20px 32–36px; border-radius: 999px; font-size: 36–42px; font-weight: 700`
  - 배경은 테마 투명 흰색(`rgba(255,255,255,0.18)`) 또는 옅은 틴트
  - 테두리는 옅은 outline (`border: 2px solid rgba(0,0,0,0.15)` 또는 반대)
- `.tag.accent` — accent 색 배경 + 대비 글자색

## GSAP 엔트런스

```js
const start = 16.8;
tl.from("#s-N .eyebrow",     { scale: 0.85, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, start + 0.2);
tl.from("#s-N .scene-title", { y: 40, opacity: 0, duration: 0.7, ease: "expo.out" }, start + 0.4);
tl.from("#s-N .tag", {
  y: 24, opacity: 0, duration: 0.45, ease: "power2.out",
  stagger: 0.08,
}, start + 0.9);
```

- 태그는 stagger로 일괄 등장 (0.06–0.1s 간격)
- accent 태그 하나만 `scale` 또는 다른 ease로 차별화해도 좋음

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [뱃지] 타이틀
보조 설명

> 태그1, *강조태그*, 태그3
```

- `>` 로 시작하는 줄이 태그 묶음
- `*키워드*`는 accent 태그로 처리

## 작성 원칙

- 태그 3~5개가 적절 (최대 8개까지 허용하되 가독성 확인)
- 각 태그는 짧은 명사구
- 강조 태그는 1개만 — 여러 개 쓰면 강조 효과가 약해짐
- 태그가 길어지면 `title-bullets`로 전환
