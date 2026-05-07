---
name: hyperframes-fx-reddit-post
description: >-
  Reddit Post Card — Reddit 포스트 카드 애니메이션 오버레이 UI 블록. 업보트·댓글 포함.
  톤: news, tech(소셜 프루프). 트리거: reddit, 레딧, social proof, 커뮤니티, 댓글 인용, upvote.
---

# Reddit Post Card

## 언제 쓰나
- 뉴스·이슈 카드에서 레딧 댓글·반응 인용
- 소셜 프루프 (상위 댓글 스크린샷 대신)
- **톤**: news, tech
- **추천 duration**: 4–5초

## 설치
```bash
npx hyperframes add reddit-post
```
→ `compositions/reddit-post.html`.

## 와이어링
```html
<div data-composition-src="compositions/reddit-post.html"
     data-start="10" data-duration="5"
     data-track-index="0"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 서브레딧·제목·본문·업보트·댓글 수는 블록 내부 설정

## 짝
- 잘 맞음: `x-post`, `tiktok-follow` (소셜 프루프 연속 카드로 구성)
- 피해야: 같은 덱에 소셜 UI 블록 너무 많이 (3개↑ 과함)
