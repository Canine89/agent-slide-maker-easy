---
name: hyperframes-fx-transitions-grid
description: >-
  Grid·tile 기반 트랜지션 쇼케이스. 화면이 타일로 쪼개지며 전환. 톤: tech,
  editorial. 트리거: grid, tile, 타일, 격자 전환, mosaic, 픽셀 모자이크, checker.
---

# Grid Transitions

## 언제 쓰나
- 테크·데이터·에디토리얼의 구조적 전환
- 타일 모자이크 감각
- **톤**: tech, minimalist / editorial
- **추천 duration**: 0.5–0.8초

## 설치
```bash
npx hyperframes add transitions-grid
```
→ `compositions/transitions-grid.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-grid.html"
     data-start="4.5" data-duration="0.7"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 그리드 사이즈·스태거 방향은 쇼케이스 내 변형

## 짝
- 잘 맞음: `grid-pixelate-wipe` (같은 미학), `sdf-iris`
- 피해야: `transitions-blur` — 구조적 vs 유기적 충돌
