---
name: hyperframes-fx-transitions-3d
description: >-
  3D perspective flip·rotate 트랜지션 쇼케이스 블록. 카드가 3D로 뒤집히며 전환.
  톤: tech, brand. 트리거: 3D, flip, rotate, 큐브, perspective, 입체 전환, cube flip.
---

# 3D Transitions

## 언제 쓰나
- 카드가 큐브처럼 뒤집히거나 3D 공간에서 회전하는 감각
- tech 제품 쇼케이스, brand 갤러리형 캐러셀
- **톤**: tech, brand
- **추천 duration**: 0.6–0.9초

## 설치
```bash
npx hyperframes add transitions-3d
```
→ `compositions/transitions-3d.html` (쇼케이스 블록, 여러 3D 변형 포함).

## 와이어링
```html
<div data-composition-src="compositions/transitions-3d.html"
     data-start="4.5" data-duration="0.8"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 회전 축·원근 거리·속도는 쇼케이스 내 변형 선택으로 조정

## 짝
- 잘 맞음: `cinematic-zoom`, `ui-3d-reveal`
- 피해야: 다른 회전형 (`swirl-vortex`) 중복
