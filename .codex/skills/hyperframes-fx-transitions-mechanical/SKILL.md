---
name: hyperframes-fx-transitions-mechanical
description: >-
  Mechanical shutter·iris 트랜지션 쇼케이스. 카메라 셔터·조리개 같은 기계적 전환.
  톤: editorial, 레트로, vintage. 트리거: shutter, iris, 셔터, 조리개, 기계적 전환,
  레트로 카메라, retro camera, clockwork.
---

# Mechanical Transitions

## 언제 쓰나
- 빈티지·레트로·필름 카메라 감성
- 에디토리얼·매거진형 카드뉴스
- **톤**: editorial(minimalist), 레트로 브랜드
- **추천 duration**: 0.5–0.8초

## 설치
```bash
npx hyperframes add transitions-mechanical
```
→ `compositions/transitions-mechanical.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-mechanical.html"
     data-start="4.5" data-duration="0.7"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 셔터 타입·방향·속도는 쇼케이스 내 변형

## 짝
- 잘 맞음: `sdf-iris`, `grain-overlay`, `light-leak`
- 피해야: `glitch` — 아날로그 감성 파괴
