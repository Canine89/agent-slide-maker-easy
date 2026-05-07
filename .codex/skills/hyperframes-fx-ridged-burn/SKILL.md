---
name: hyperframes-fx-ridged-burn
description: >-
  Ridged Burn — 터뷸런스 태움 효과 트랜지션. 화면이 불타듯 사라진다.
  톤: news, emotional (강한 감정). 트리거: burn, 태움, 불타는 전환, 터뷸런스,
  destruction, 격정, 강렬한 전환.
---

# Ridged Burn

## 언제 쓰나
- 격정적 뉴스·폭로·사회 이슈에서 "불타는" 감각
- 스포츠·액션처럼 "열기" 메타포
- **톤**: news, emotional (강도 높음)
- **추천 duration**: 0.6–0.9초

## 설치
```bash
npx hyperframes add ridged-burn
```
→ `compositions/ridged-burn.html`.

## 와이어링
```html
<div data-composition-src="compositions/ridged-burn.html"
     data-start="4.5" data-duration="0.8"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 불꽃 색·터뷸런스 스케일·burn-in 속도는 shader 내부

## 짝
- 잘 맞음: `flash-through-white`, `glitch` (강한 news)
- 피해야: brand·minimalist — 너무 강한 감각으로 톤 파괴
