---
name: hyperframes-fx-transitions-distortion
description: >-
  Warp·distortion 트랜지션 쇼케이스. 씬이 왜곡되며 넘어간다. 톤: tech, news, 실험적.
  트리거: distortion, 왜곡, warp, 실험적 전환, 사이키델릭, psychedelic.
---

# Distortion Transitions

## 언제 쓰나
- 실험적·사이키델릭·artsy 톤
- tech·AI의 "현실 왜곡" 메타포
- **톤**: tech, news, 실험적 콘텐츠
- **추천 duration**: 0.6–0.9초

## 설치
```bash
npx hyperframes add transitions-distortion
```
→ `compositions/transitions-distortion.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-distortion.html"
     data-start="4.4" data-duration="0.8"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 왜곡 종류·강도는 쇼케이스 내 변형 선택

## 짝
- 잘 맞음: `glitch`, `chromatic-radial-split`
- 피해야: minimalist·emotional 톤
