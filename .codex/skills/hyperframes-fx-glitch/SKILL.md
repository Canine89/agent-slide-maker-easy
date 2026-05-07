---
name: hyperframes-fx-glitch
description: >-
  Glitch — 디지털 글리치 아티팩트 트랜지션. 화면이 깨지듯 찢어지며 전환. 톤: news,
  tech. 트리거: glitch, 글리치, 디지털 노이즈, 아티팩트, 깨지는 전환, 해킹, 오류.
---

# Glitch

## 언제 쓰나
- 뉴스·사건·폭로형 카드뉴스에서 "뭔가 잘못됐다" 긴장감
- 해킹·오류·시스템 다운 같은 테크 메타포
- **톤**: news, tech
- **추천 duration**: 0.4–0.7초

## 설치
```bash
npx hyperframes add glitch
```
→ `compositions/glitch.html`.

## 와이어링
```html
<div data-composition-src="compositions/glitch.html"
     data-start="4.6" data-duration="0.6"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 글리치 강도·RGB 변위·스캔라인은 shader 내부

## 짝
- 잘 맞음: `chromatic-radial-split`, `flash-through-white` (news/tech 조합)
- 피해야: brand·emotional·minimalist 톤에 남용 금지 — 덱 톤을 깨뜨림
