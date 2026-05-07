---
name: hyperframes-fx-transitions-radial
description: >-
  Radial wipe·reveal 트랜지션 쇼케이스. 중심에서 방사형으로 화면을 걷어낸다.
  톤: tech, brand. 트리거: radial, 방사형, wipe, reveal, circle sweep, 원형 전환.
---

# Radial Transitions

## 언제 쓰나
- 중심 포인트에서 방사형으로 리빌하는 감각
- 테크 "디스커버리" 느낌, 브랜드 로고 리빌
- **톤**: tech, brand
- **추천 duration**: 0.5–0.8초

## 설치
```bash
npx hyperframes add transitions-radial
```
→ `compositions/transitions-radial.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-radial.html"
     data-start="4.5" data-duration="0.7"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 중심점·방사 방향(inside-out / outside-in)은 쇼케이스 변형

## 짝
- 잘 맞음: `sdf-iris` (홍채와 결합), `transitions-scale`
- 피해야: `swirl-vortex` — 같은 원형 감각 중복
