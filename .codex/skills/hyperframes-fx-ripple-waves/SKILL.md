---
name: hyperframes-fx-ripple-waves
description: >-
  Ripple Waves — 동심원 물결 왜곡 트랜지션. 물방울이 떨어진 듯한 파문.
  톤: emotional, brand. 트리거: ripple, wave, 파문, 물결, 수면, 잔물결, 임팩트 포인트,
  organic transition.
---

# Ripple Waves

## 언제 쓰나
- 감성·회고·추억 테마에서 "파장이 번진다" 메타포
- 음악·사운드·명상 콘텐츠
- **톤**: emotional, brand
- **추천 duration**: 0.6–0.9초

## 설치
```bash
npx hyperframes add ripple-waves
```
→ `compositions/ripple-waves.html`.

## 와이어링
```html
<div data-composition-src="compositions/ripple-waves.html"
     data-start="4.5" data-duration="0.8"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 파문 중심점·주파수·감쇠율은 shader 내부

## 짝
- 잘 맞음: `light-leak`, `domain-warp-dissolve`, `transitions-blur`
- 피해야: `glitch`, `flash-through-white` — 감성과 충돌
