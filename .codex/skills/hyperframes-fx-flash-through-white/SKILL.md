---
name: hyperframes-fx-flash-through-white
description: >-
  Flash Through White — 흰빛 플래시 크로스페이드. 씬 사이 한 프레임 흰빛으로 번쩍.
  톤: news, tech. 트리거: flash, 플래시, 흰빛 전환, 번쩍, white flash, 하드컷, 급전환.
---

# Flash Through White

## 언제 쓰나
- 극적 리빌·사건 전환·뉴스 속보 느낌
- 두 씬이 완전히 다른 장면으로 갑자기 바뀔 때
- **톤**: news, tech (브랜드에는 약간 강함)
- **추천 duration**: 0.3–0.5초

## 설치
```bash
npx hyperframes add flash-through-white
```
→ `compositions/flash-through-white.html`.

## 와이어링
```html
<div data-composition-src="compositions/flash-through-white.html"
     data-start="4.8" data-duration="0.4"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 플래시 강도·색조는 내부 shader 변수에서 조정

## 짝
- 잘 맞음: `glitch`, `chromatic-radial-split`, `whip-pan` (news 트리오)
- 피해야: `light-leak` 동시 사용 — 둘 다 빛 기반이라 방해
