---
name: hyperframes-fx-transitions-scale
description: >-
  Scale·zoom 트랜지션 쇼케이스. 씬이 커지거나 작아지며 전환. 톤: 모든 톤 OK.
  트리거: scale, zoom, 줌, 확대, 축소, scale up, scale down, Ken Burns.
---

# Scale Transitions

## 언제 쓰나
- 가장 범용적인 스케일 전환 (줌인·줌아웃)
- minimalist 톤에 깔끔한 대표 선택
- **톤**: 모든 톤
- **추천 duration**: 0.4–0.8초

## 설치
```bash
npx hyperframes add transitions-scale
```
→ `compositions/transitions-scale.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-scale.html"
     data-start="4.6" data-duration="0.6"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 스케일 방향(in/out)·비율·이징은 쇼케이스 변형

## 짝
- 잘 맞음: 어디나 — 특히 `cinematic-zoom`과 결합
- 피해야: 특별히 없음
