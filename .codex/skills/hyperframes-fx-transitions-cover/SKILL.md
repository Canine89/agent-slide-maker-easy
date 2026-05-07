---
name: hyperframes-fx-transitions-cover
description: >-
  Cover/uncover 슬라이드 트랜지션 쇼케이스. 새 씬이 이전 씬을 덮거나 걷어낸다.
  톤: tech, brand, minimalist. 트리거: cover, slide, 덮기, 걷기, reveal slide,
  deck 스타일, 프리젠테이션 전환.
---

# Cover Transitions

## 언제 쓰나
- 프리젠테이션·딕(deck) 스타일의 깔끔한 슬라이드 전환
- 카드 방향성이 확실한 흐름 (왼쪽 → 오른쪽, 아래 → 위)
- **톤**: tech, brand, minimalist
- **추천 duration**: 0.4–0.7초

## 설치
```bash
npx hyperframes add transitions-cover
```
→ `compositions/transitions-cover.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-cover.html"
     data-start="4.6" data-duration="0.5"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 방향·이징은 쇼케이스 내 변형 선택

## 짝
- 잘 맞음: `transitions-push`, `transitions-scale`
- 피해야: `transitions-distortion`, `glitch` — 깔끔함 파괴
