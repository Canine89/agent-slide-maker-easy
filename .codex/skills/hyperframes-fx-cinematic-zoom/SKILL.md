---
name: hyperframes-fx-cinematic-zoom
description: >-
  Cinematic Zoom — 드라마틱 줌 블러 트랜지션. 카메라가 주제로 빨려드는 느낌.
  톤: tech, brand. 트리거: zoom, 줌, 시네마틱 줌, 줌 블러, 클로즈업 전환, dramatic.
---

# Cinematic Zoom

## 언제 쓰나
- 어떤 대상을 클로즈업하며 다음 씬으로 전환할 때
- 제품 샷 → 상세 설명, 인물 → 인용구 등 "들여다보기" 리듬
- **톤**: tech, brand, minimalist
- **추천 duration**: 0.6–0.9초 (줌이 느껴지려면 약간 길게)

## 설치
```bash
npx hyperframes add cinematic-zoom
```
→ `compositions/cinematic-zoom.html`.

## 와이어링
```html
<div data-composition-src="compositions/cinematic-zoom.html"
     data-start="4.5" data-duration="0.8"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 줌 스케일·블러 강도·이징은 shader 내부

## 짝
- 잘 맞음: `sdf-iris`, `chromatic-radial-split` (tech)
- 피해야: `whip-pan` 바로 옆 — 둘 다 카메라 움직임이라 혼란
