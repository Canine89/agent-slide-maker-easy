---
name: hyperframes-fx-chromatic-radial-split
description: >-
  Chromatic Radial Split — RGB 분리 + 방사형 찢김 트랜지션. 톤: tech, news. 트리거:
  chromatic, 색수차, RGB split, 색 분리, glitch, 테크 전환, 미래 느낌, split.
---

# Chromatic Radial Split

## 언제 쓰나
- 테크·AI·데이터 주제에서 현대적 임팩트
- 뉴스에서 "긴박한 색 분리" 효과
- **톤**: tech, news
- **추천 duration**: 0.4–0.6초

## 설치
```bash
npx hyperframes add chromatic-radial-split
```
→ `compositions/chromatic-radial-split.html`.

## 와이어링
```html
<div data-composition-src="compositions/chromatic-radial-split.html"
     data-start="4.7" data-duration="0.5"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 색 분리 강도·방사형 중심점은 shader 내부에서 조정

## 짝
- 잘 맞음: `glitch`, `sdf-iris`, `cinematic-zoom` (tech 트리오)
- 피해야: brand·emotional 톤에는 사용 자제 — 감성 약화
