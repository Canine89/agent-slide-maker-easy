---
name: hyperframes-fx-transitions-dissolve
description: >-
  Dissolve·페이드 트랜지션 쇼케이스. 가장 기본적인 씬 교체. 톤: 모든 톤 OK.
  트리거: dissolve, 디졸브, fade, 페이드, 기본 전환, safe transition.
---

# Dissolve Transitions

## 언제 쓰나
- 어떤 톤에나 맞는 안전한 기본 전환
- 다른 강한 트랜지션 사이에 "숨 고르기" 용도
- **톤**: 모든 톤
- **추천 duration**: 0.4–0.8초

## 설치
```bash
npx hyperframes add transitions-dissolve
```
→ `compositions/transitions-dissolve.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-dissolve.html"
     data-start="4.6" data-duration="0.5"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 페이드 이징·색조는 쇼케이스 내 변형에서 선택

## 짝
- 잘 맞음: 어디나
- 피해야: 특별히 없음 — 가장 무난
