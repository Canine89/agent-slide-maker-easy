---
name: hyperframes-slide-work-title-image
description: >-
  HyperFrames 컴포지션의 title-image 슬라이드 전용 스킬. 큰 제목과 단일 대표 이미지를
  조합하는 슬라이드를 HTML + GSAP으로 설계하거나 수정할 때 사용.
---

# Title Image Slide (HyperFrames)

## 언제 쓰나

- 큰 제목과 대표 이미지 한 장이 메시지의 중심일 때
- 표지, 제품 소개, 서비스 소개, 스크린샷 소개

## HTML 구조

```html
<div id="s-N" class="scene clip title-image"
     data-start="..." data-duration="6" data-track-index="0">
  <div class="eyebrow">카테고리</div>
  <div class="scene-title">메인 타이틀</div>
  <div class="scene-subtitle">보조 설명 (선택)</div>
  <div class="image-frame">
    <img src="assets/01-image-name.png" alt="설명" crossorigin="anonymous" />
  </div>
</div>
```

## CSS 핵심

- `.scene.title-image` — `align-items: center; text-align: center` (세로 중앙 정렬, 수평 중앙)
- `.image-frame` — `width: 100%; max-width: 1400px; aspect-ratio: 16/9`, `margin-top: 48px`, 모서리 둥글기 선택
- `.image-frame img` — `width: 100%; height: 100%; object-fit: contain`
- 이미지가 없을 때 대비 `.image-frame`에 테마 반투명 배경(`rgba(255,255,255,0.06)`)과 dashed border로 자체 placeholder 스타일 지정

## GSAP 엔트런스

```js
const start = 11.2;
tl.from("#s-N .eyebrow",        { y: -15, opacity: 0, duration: 0.5, ease: "power3.out" }, start + 0.2);
tl.from("#s-N .scene-title",    { y: 40,  opacity: 0, duration: 0.7, ease: "expo.out"   }, start + 0.4);
tl.from("#s-N .scene-subtitle", {         opacity: 0, duration: 0.6, ease: "power2.out" }, start + 0.9);
tl.from("#s-N .image-frame",    { y: 60, opacity: 0, scale: 0.95, duration: 0.9, ease: "power3.out" }, start + 1.2);
```

- 이미지는 **아래에서 위로** 올라오며 살짝 스케일 업이 기본
- 제목 → 서브텍스트 → 이미지 순서 유지

## 레이아웃

- 세로 중앙 정렬: 뱃지 → 제목 → 서브텍스트 → 이미지 순으로 위에서 아래로 쌓임
- 모든 요소가 수평 중앙 정렬
- `position: absolute` 이미지 지양 — 플로우 안에서 크기 관리

## 마크다운 감지 규칙 (생성기 구축 시)

```markdown
# [뱃지] 타이틀
서브텍스트

![](01-image.png)
```

## 작성 원칙

- 제목이 주인공이고 이미지는 보조 증거
- 이미지는 프로젝트 `assets/` 아래에 두고 상대경로로 참조
- 이미지 파일명은 `01-slide-description.png`처럼 `번호-설명.확장자` 규칙 권장
- 서브텍스트는 1~2줄로 짧게 유지
- 이미지가 강하면 제목은 더 짧게, 이미지가 약하면 제목을 명확하게

## 이미지가 없을 때

- 비어 있는 `.image-frame` 자체에 dashed border + 옅은 배경을 두어 "이 자리에 이미지가 들어온다"를 시각적으로 표시
- 자동 placeholder 컴포넌트는 없음 — CSS 기본값이 placeholder 역할
- 실제 이미지가 준비되면 `<img>`만 채워 넣으면 됨
