---
name: hyperframes-fx-yt-lower-third
description: >-
  YouTube Lower Third — 유튜브 구독 버튼 + 아바타 + 채널 정보 애니메이션 로워서드
  UI 블록. 톤: brand, news(유튜브 연동). 트리거: youtube, 유튜브 구독, lower third,
  subscribe CTA, 채널 홍보, YT branding.
---

# YouTube Lower Third

## 언제 쓰나
- 인스타 카드뉴스에서 유튜브 채널 크로스 프로모션
- 구독 유도 카드
- **톤**: brand, news
- **추천 duration**: 3–5초

## 설치
```bash
npx hyperframes add yt-lower-third
```
→ `compositions/yt-lower-third.html`.

## 와이어링 (하단 로워서드)
```html
<div data-composition-src="compositions/yt-lower-third.html"
     data-start="18" data-duration="2"
     data-track-index="3"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 채널 아바타·이름·구독 버튼 텍스트는 블록 내부 설정

## 짝
- 잘 맞음: `logo-outro`와 분리된 카드로
- 피해야: `instagram-follow`, `tiktok-follow` 동시 — CTA 중복
