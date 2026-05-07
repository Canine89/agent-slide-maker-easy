---
name: hyperframes-fx-x-post
description: >-
  X Post Card — X(Twitter) 포스트 카드 애니메이션 오버레이 UI 블록. 리트윗·좋아요
  수치 포함. 톤: news, tech. 트리거: X post, twitter, 트위터, 인용 트윗, 소셜 프루프,
  tweet card, quote tweet.
---

# X Post Card

## 언제 쓰나
- 뉴스·이슈에서 X(트위터) 인용으로 소셜 프루프
- 인플루언서·뉴스 계정 트윗 강조
- **톤**: news, tech
- **추천 duration**: 4–5초

## 설치
```bash
npx hyperframes add x-post
```
→ `compositions/x-post.html`.

## 와이어링
```html
<div data-composition-src="compositions/x-post.html"
     data-start="10" data-duration="5"
     data-track-index="0"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 프로필·본문·수치는 블록 내부 설정

## 짝
- 잘 맞음: `reddit-post` (소셜 프루프 연속)
- 피해야: 소셜 블록 3개↑ 동시 — 과부하
