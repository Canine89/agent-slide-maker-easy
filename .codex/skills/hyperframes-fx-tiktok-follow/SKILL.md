---
name: hyperframes-fx-tiktok-follow
description: >-
  TikTok Follow — 애니메이션 TikTok 팔로우 프로필 카드 + 버튼 오버레이 UI 블록.
  톤: brand, news(소셜 CTA). 트리거: tiktok, 틱톡 팔로우, TikTok CTA, 크로스 프로모션,
  short form CTA.
---

# TikTok Follow

## 언제 쓰나
- 인스타 카드뉴스에서 TikTok 크로스 프로모션
- 젊은 타깃 브랜드 마감 CTA
- **톤**: brand, news (젊은 톤)
- **추천 duration**: 3–5초

## 설치
```bash
npx hyperframes add tiktok-follow
```
→ `compositions/tiktok-follow.html`.

## 와이어링
```html
<div data-composition-src="compositions/tiktok-follow.html"
     data-start="18" data-duration="2"
     data-track-index="3"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 프로필 이미지·핸들·버튼 텍스트는 블록 내부

## 짝
- 잘 맞음: `logo-outro` 전후
- 피해야: `instagram-follow`, `yt-lower-third` 동시 — CTA 중복
