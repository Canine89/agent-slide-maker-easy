---
name: hyperframes-fx-sdf-iris
description: >-
  SDF Iris — Signed Distance Field 홍채 열림/닫힘 트랜지션. 카메라 조리개가
  열리듯 새 씬이 드러난다. 톤: brand, tech. 트리거: iris, 홍채, 조리개, 리빌,
  reveal, 열림, 닫힘, vintage camera, pro reveal.
---

# SDF Iris

## 언제 쓰나
- 질문 → 답 공개 같은 "리빌" 리듬에 최적 (question → stat 전환)
- 빈티지 카메라 iris 감성
- **톤**: brand, tech
- **추천 duration**: 0.5–0.8초

## 설치
```bash
npx hyperframes add sdf-iris
```
→ `compositions/sdf-iris.html`.

## 와이어링
```html
<div data-composition-src="compositions/sdf-iris.html"
     data-start="4.6" data-duration="0.6"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- iris 중심·열림 속도·경계 두께는 shader 내부

## 짝
- 잘 맞음: `whip-pan`, `light-leak`, `cinematic-zoom`
- 피해야: `transitions-radial` — 둘 다 방사형이라 중복
