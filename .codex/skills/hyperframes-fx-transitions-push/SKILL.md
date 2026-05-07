---
name: hyperframes-fx-transitions-push
description: >-
  Push·slide 트랜지션 쇼케이스. 새 씬이 이전 씬을 밀어낸다. 톤: tech, brand,
  minimalist. 트리거: push, slide, 밀어내기, 슬라이드, 방향 전환, carousel slide.
---

# Push Transitions

## 언제 쓰나
- 캐러셀 스와이프 느낌의 자연스런 방향성 전환
- 정보 나열 흐름 (step-by-step)
- **톤**: tech, brand, minimalist
- **추천 duration**: 0.4–0.6초

## 설치
```bash
npx hyperframes add transitions-push
```
→ `compositions/transitions-push.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-push.html"
     data-start="4.6" data-duration="0.5"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 방향(좌/우/상/하)·이징은 쇼케이스 내 변형

## 짝
- 잘 맞음: `transitions-cover`, `transitions-scale`
- 피해야: `swirl-vortex` — 방향감 혼란
