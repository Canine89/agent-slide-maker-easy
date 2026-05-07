---
name: hyperframes-fx-app-showcase
description: >-
  App Showcase — 3개 스마트폰이 플로팅되며 앱 화면을 보여주는 UI 블록. 톤: tech,
  brand(제품). 트리거: app showcase, 앱 소개, 프로덕트 쇼케이스, 스마트폰 목업, 3 screens, device mockup.
---

# App Showcase

## 언제 쓰나
- 앱·SaaS·모바일 제품 출시·기능 소개
- 3개 디바이스 동시 노출로 기능 다양성 강조
- **톤**: tech, brand(제품 테크)
- **추천 duration**: 5–7초 (카드 1장 분량)

## 설치
```bash
npx hyperframes add app-showcase
```
→ `compositions/app-showcase.html`.

## 와이어링 (카드 전체를 대체)
```html
<div data-composition-src="compositions/app-showcase.html"
     data-start="5" data-duration="5"
     data-track-index="0"
     data-width="1080" data-height="1350">
</div>
```

앱 스크린샷은 `compositions/app-showcase.html` 내부에서 참조. `assets/screen-1.png` 등으로 교체.

## 파라미터
- 스크린 이미지·플로팅 각도·색상은 블록 내부 편집

## 짝
- 잘 맞음: `cinematic-zoom`으로 이 블록에 진입, `logo-outro` 로 마감
- 피해야: emotional 톤과 어울리지 않음
