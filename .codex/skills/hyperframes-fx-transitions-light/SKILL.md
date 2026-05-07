---
name: hyperframes-fx-transitions-light
description: >-
  Light·glow·flash 트랜지션 쇼케이스. 빛이 번지며 전환. 톤: brand, news, emotional.
  트리거: light, glow, flash, 빛, 글로우, 플래시, 섬광, radiant, luminous.
---

# Light Transitions

## 언제 쓰나
- 고급스런 브랜드 전환 (bright glow)
- 뉴스 속보 (sharp flash)
- 감성 마감 (soft glow)
- **톤**: brand, news, emotional — 빛의 성격으로 분기
- **추천 duration**: 0.5–0.9초

## 설치
```bash
npx hyperframes add transitions-light
```
→ `compositions/transitions-light.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-light.html"
     data-start="4.5" data-duration="0.7"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 빛 색·범위·플래시 강도는 쇼케이스 내 변형

## 짝
- 잘 맞음: `light-leak`, `shimmer-sweep`
- 피해야: `flash-through-white` 중복
