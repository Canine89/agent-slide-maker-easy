---
name: hyperframes-fx-spotify-card
description: >-
  Spotify Card — Spotify 플레이어 now-playing 카드 애니메이션 오버레이. 앨범 아트
  + 재생 진행바. 톤: brand, emotional(음악 콘텐츠). 트리거: spotify, 스포티파이,
  music card, 음악 플레이어, now playing, 앨범 카드.
---

# Spotify Card

## 언제 쓰나
- 음악·플레이리스트·팟캐스트 콘텐츠
- brand 협업·음악 큐레이션
- **톤**: brand(음악), emotional
- **추천 duration**: 4–5초

## 설치
```bash
npx hyperframes add spotify-card
```
→ `compositions/spotify-card.html`.

## 와이어링
```html
<div data-composition-src="compositions/spotify-card.html"
     data-start="10" data-duration="5"
     data-track-index="0"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 앨범 아트·곡명·아티스트·진행률은 블록 내부 설정

## 짝
- 잘 맞음: `grain-overlay`, `light-leak` (음악 감성)
- 피해야: tech 하드 톤과 어울리지 않음
