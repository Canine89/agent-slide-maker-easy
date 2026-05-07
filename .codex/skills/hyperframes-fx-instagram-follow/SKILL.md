---
name: hyperframes-fx-instagram-follow
description: >-
  Instagram Follow — 애니메이션 팔로우 프로필 카드 오버레이 UI 블록. 카드뉴스
  마감 CTA에 사용. 톤: brand, news(소셜 CTA). 트리거: instagram follow, 인스타 팔로우,
  팔로우 CTA, 프로필 카드, social CTA.
---

# Instagram Follow

## 언제 쓰나
- 카드뉴스 마지막 카드에 "팔로우 해주세요" 콜투액션
- 인스타 계정 프로모션
- **톤**: brand, news
- **추천 duration**: 3–5초

## 설치
```bash
npx hyperframes add instagram-follow
```
→ `compositions/instagram-follow.html`.

## 와이어링 (보통 마지막 카드 위에 오버레이)
```html
<!-- 마지막 카드 마감 구간에 떠오르게 -->
<div data-composition-src="compositions/instagram-follow.html"
     data-start="18" data-duration="2"
     data-track-index="3"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 프로필 이미지·핸들·팔로워 수·버튼 문구는 블록 내부에서 설정

## 짝
- 잘 맞음: `logo-outro` 대신 또는 함께
- 피해야: 여러 소셜 CTA 동시 (TikTok·YouTube·X 중복) — 하나만 선택
