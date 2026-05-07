---
name: hyperframes-fx-data-chart
description: >-
  Data Chart — NYT 스타일 대형 타이포 수치 스태거 리빌 UI 블록. 데이터 시각화
  리빌에 쓴다. 톤: tech, news(데이터 저널리즘). 트리거: chart, 차트, 데이터 시각화,
  수치 애니메이션, NYT style, data reveal, stat animation.
---

# Data Chart

## 언제 쓰나
- 데이터 저널리즘 스타일의 수치 공개 카드 (stat 대체)
- 여러 지표를 순차 리빌하며 비교할 때
- **톤**: tech, news(데이터 저널리즘)
- **추천 duration**: 5–7초

## 설치
```bash
npx hyperframes add data-chart
```
→ `compositions/data-chart.html`.

## 와이어링
```html
<div data-composition-src="compositions/data-chart.html"
     data-start="10" data-duration="5"
     data-track-index="0"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 수치·라벨·차트 타입은 블록 내부 JS 변수로 설정

## 짝
- 잘 맞음: `chromatic-radial-split`으로 진입, `sdf-iris`로 마감
- 피해야: 이미 카드뉴스 `stat` 템플릿과 중복 — 둘 중 하나만 선택
