---
name: hyperframes-fx-whip-pan
description: >-
  Whip Pan 씬 트랜지션 — 빠른 카메라 휘젓기로 씬 교체. 톤: brand, news. 트리거:
  whip, 휙, 휘젓기, 카메라 팬, 급제동, 에너지 전환, 브랜드 전환, news transition.
---

# Whip Pan

## 언제 쓰나
- 빠른 카메라 휘젓기 질감, 에너지 있는 리듬
- photo-cover → question 처럼 "후킹 → 급제동" 전환에 최적
- **톤**: brand, news
- **추천 duration**: 0.4–0.6초

## 설치
```bash
npx hyperframes add whip-pan
```
→ `compositions/whip-pan.html` 생성.

## 와이어링 (카드 N 끝 → 카드 N+1 시작 overlap)
```html
<!-- 예: 카드 1(0~5s) → 카드 2(5~10s), 트랜지션 4.7~5.2s -->
<div data-composition-src="compositions/whip-pan.html"
     data-start="4.7" data-duration="0.5"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- duration·블러 강도·방향은 `compositions/whip-pan.html` 내부 shader 소스에서 조정

## 짝
- 잘 맞음: `grain-overlay`, `shimmer-sweep`, `light-leak` (다른 전환과 섞어 3-trio)
- 피해야: 같은 덱에 `swirl-vortex` 중복 — 둘 다 회전감이라 과함
