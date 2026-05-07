---
name: hyperframes-fx-logo-outro
description: >-
  Logo Outro — 시네마틱 로고 리빌 + 글로우 + 태그라인 페이드인 UI 블록.
  카드뉴스·영상 마감에 사용. 톤: brand. 트리거: logo outro, 로고 리빌, 마감 로고,
  브랜드 아웃로, closing logo, 태그라인.
---

# Logo Outro

## 언제 쓰나
- 카드뉴스 / 영상 **마지막 카드 대체**
- 브랜드 정체성 마감
- **톤**: brand (가장 잘 맞음)
- **추천 duration**: 4–6초

## 설치
```bash
npx hyperframes add logo-outro
```
→ `compositions/logo-outro.html`.

## 와이어링 (마지막 카드 자리에 그대로 대체)
```html
<!-- 기존 cover closing 카드 대신 -->
<div data-composition-src="compositions/logo-outro.html"
     data-start="15" data-duration="5"
     data-track-index="0"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 로고 이미지·태그라인 문구·글로우 색은 블록 내부 설정

## 짝
- 잘 맞음: `light-leak`으로 진입, `grain-overlay` 유지
- 피해야: 추가 CTA 오버레이 중복
