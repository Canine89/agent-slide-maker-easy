---
name: hyperframes-fx-thermal-distortion
description: >-
  Thermal Distortion — 열기 아지랑이 열왜곡 트랜지션. 사막의 신기루 같은 질감.
  톤: editorial(emotional), 여름·열대 테마. 트리거: thermal, heat haze, 아지랑이,
  신기루, mirage, 열기, 사막, 한여름, 열대.
---

# Thermal Distortion

## 언제 쓰나
- 한여름·열대·사막·요리·온열 테마의 감성적 전환
- 뜨거움·열정의 은유 (연애·뜨거운 이슈)
- **톤**: emotional / 특정 주제 (여행·요리)
- **추천 duration**: 0.7–1.0초

## 설치
```bash
npx hyperframes add thermal-distortion
```
→ `compositions/thermal-distortion.html`.

## 와이어링
```html
<div data-composition-src="compositions/thermal-distortion.html"
     data-start="4.4" data-duration="0.9"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 열 왜곡 강도·주파수·방향은 shader 내부

## 짝
- 잘 맞음: `light-leak`, `grain-overlay`, `ripple-waves`
- 피해야: `glitch`, `flash-through-white` — 질감 정반대
