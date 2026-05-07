---
name: hyperframes-fx-transitions-blur
description: >-
  Blur 기반 트랜지션 쇼케이스. 가우시안/모션 블러로 씬을 부드럽게 넘긴다.
  톤: emotional, minimalist, brand. 트리거: blur, 블러, 흐림, 부드러운 전환,
  soft transition, motion blur.
---

# Blur Transitions

## 언제 쓰나
- 감성·에디토리얼 카드의 부드러운 호흡 전환
- 사진 중심 카드에서 다음 씬으로 녹이듯 넘어갈 때
- **톤**: emotional, minimalist, brand
- **추천 duration**: 0.6–1.0초

## 설치
```bash
npx hyperframes add transitions-blur
```
→ `compositions/transitions-blur.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-blur.html"
     data-start="4.3" data-duration="0.9"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 블러 강도·종류(gaussian / motion)는 쇼케이스 내에서 선택

## 짝
- 잘 맞음: `light-leak`, `domain-warp-dissolve`, `grain-overlay`
- 피해야: `glitch`, `flash-through-white` — 부드러움과 충돌
