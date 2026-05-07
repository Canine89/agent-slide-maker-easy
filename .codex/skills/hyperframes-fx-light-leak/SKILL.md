---
name: hyperframes-fx-light-leak
description: >-
  Light Leak — 시네마틱 라이트 리크 오버레이 전환. 필름 카메라의 빛 새임 느낌.
  톤: brand, emotional. 트리거: light leak, 라이트 리크, 빛 새임, 필름, 시네마틱,
  따뜻한 전환, vintage, analog.
---

# Light Leak

## 언제 쓰나
- 브랜드·라이프스타일·감성 콘텐츠의 "따뜻한 마감" 전환
- 아날로그/빈티지/필름 감성
- stat → image-feature 처럼 "숫자 → 스토리" 호흡 완화 지점에 최적
- **톤**: brand, emotional
- **추천 duration**: 0.7–1.0초

## 설치
```bash
npx hyperframes add light-leak
```
→ `compositions/light-leak.html`.

## 와이어링
```html
<div data-composition-src="compositions/light-leak.html"
     data-start="4.4" data-duration="0.9"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 리크 색(따뜻한 주황/골드 기본)·강도·방향은 shader 내부

## 짝
- 잘 맞음: `grain-overlay`, `whip-pan`, `transitions-blur`
- 피해야: `flash-through-white` — 둘 다 빛 기반이라 중복
