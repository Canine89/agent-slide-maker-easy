---
name: hyperframes-fx-cross-warp-morph
description: >-
  Cross Warp Morph — 교차 워프 모핑 트랜지션. 두 씬이 서로를 변형하며 녹아든다.
  톤: minimalist, emotional. 트리거: morph, warp, 모핑, 형태 변형, 부드러운 전환.
---

# Cross Warp Morph

## 언제 쓰나
- 매거진·에디토리얼·감성 콘텐츠의 부드러운 전환
- 두 씬의 색감·형태가 비슷해서 경계를 흐리고 싶을 때
- **톤**: minimalist, emotional
- **추천 duration**: 0.7–1.0초 (느긋하게)

## 설치
```bash
npx hyperframes add cross-warp-morph
```
→ `compositions/cross-warp-morph.html`.

## 와이어링
```html
<div data-composition-src="compositions/cross-warp-morph.html"
     data-start="4.3" data-duration="0.9"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 워프 강도·모핑 포인트는 shader 내부

## 짝
- 잘 맞음: `transitions-blur`, `domain-warp-dissolve`, `transitions-scale`
- 피해야: `glitch`, `flash-through-white` — 성격 정반대라 톤 파괴
