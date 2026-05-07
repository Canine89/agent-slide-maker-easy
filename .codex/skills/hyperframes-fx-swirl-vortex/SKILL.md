---
name: hyperframes-fx-swirl-vortex
description: >-
  Swirl Vortex — 소용돌이 왜곡 트랜지션. 화면이 소용돌이치며 다음 씬으로 빨려든다.
  톤: news, tech. 트리거: swirl, vortex, 소용돌이, 토네이도, 회오리, 에너지 전환, spiral.
---

# Swirl Vortex

## 언제 쓰나
- "빨려드는" 감각의 에너지 전환 (사건·폭로·긴박한 뉴스)
- 토네이도·허리케인·혼란 메타포
- **톤**: news, tech
- **추천 duration**: 0.6–0.9초

## 설치
```bash
npx hyperframes add swirl-vortex
```
→ `compositions/swirl-vortex.html`.

## 와이어링
```html
<div data-composition-src="compositions/swirl-vortex.html"
     data-start="4.5" data-duration="0.8"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 회전 속도·소용돌이 중심·강도는 shader 내부

## 짝
- 잘 맞음: `glitch`, `flash-through-white` (news)
- 피해야: `whip-pan` — 둘 다 회전감이라 과함
