---
name: hyperframes-fx-domain-warp-dissolve
description: >-
  Domain Warp Dissolve — 프랙탈 노이즈 도메인 워프 디졸브. 자연스러운 흐물거림으로
  씬 교체. 톤: minimalist, emotional. 트리거: dissolve, 디졸브, 워프, 프랙탈,
  자연스러운 전환, organic transition.
---

# Domain Warp Dissolve

## 언제 쓰나
- 흐르는 물·연기·안개 같은 자연스러운 질감의 전환
- 에디토리얼·감성 콘텐츠에서 호흡을 길게 끌고 싶을 때
- **톤**: minimalist, emotional
- **추천 duration**: 0.8–1.2초

## 설치
```bash
npx hyperframes add domain-warp-dissolve
```
→ `compositions/domain-warp-dissolve.html`.

## 와이어링
```html
<div data-composition-src="compositions/domain-warp-dissolve.html"
     data-start="4.2" data-duration="1.0"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 노이즈 주파수·워프 스케일·속도는 shader 내부

## 짝
- 잘 맞음: `transitions-blur`, `ripple-waves`, `cross-warp-morph`
- 피해야: `flash-through-white`, `whip-pan` — 빠른 효과와 리듬 충돌
