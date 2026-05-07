---
name: hyperframes-fx-ui-3d-reveal
description: >-
  3D UI Reveal — 퍼스펙티브 3D 리빌 애니메이션 UI 블록. UI 요소가 입체적으로
  등장. 톤: tech, brand(제품). 트리거: 3D UI, 3D reveal, 입체 등장, perspective,
  제품 리빌, UI 등장, product showcase.
---

# 3D UI Reveal

## 언제 쓰나
- 앱 화면·디자인·UI 목업을 3D로 등장시킬 때
- 제품 쇼케이스의 여러 화면 동시 소개
- **톤**: tech, brand(제품)
- **추천 duration**: 4–6초

## 설치
```bash
npx hyperframes add ui-3d-reveal
```
→ `compositions/ui-3d-reveal.html`.

## 와이어링
```html
<div data-composition-src="compositions/ui-3d-reveal.html"
     data-start="5" data-duration="5"
     data-track-index="0"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- UI 이미지·회전 각도·등장 순서는 블록 내부 설정

## 짝
- 잘 맞음: `cinematic-zoom`, `app-showcase` (테크 제품 덱)
- 피해야: `glitch`, `destruction` — 깔끔한 3D 반복 방해
