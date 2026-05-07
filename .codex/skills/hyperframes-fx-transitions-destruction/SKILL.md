---
name: hyperframes-fx-transitions-destruction
description: >-
  Destructive break-apart 트랜지션 쇼케이스. 씬이 깨지거나 폭발하며 전환.
  톤: news, tech(에너지). 트리거: destruction, 깨짐, 폭발, shatter, 파괴, 액션,
  드라마틱 파괴, break apart.
---

# Destruction Transitions

## 언제 쓰나
- 사건·폭로·스포츠·액션형 콘텐츠
- "깨지는" 극적 메타포
- **톤**: news, 액션 테크
- **추천 duration**: 0.6–0.9초

## 설치
```bash
npx hyperframes add transitions-destruction
```
→ `compositions/transitions-destruction.html`.

## 와이어링
```html
<div data-composition-src="compositions/transitions-destruction.html"
     data-start="4.4" data-duration="0.8"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 파편 개수·중력·방향은 쇼케이스 내 변형에서 선택

## 짝
- 잘 맞음: `ridged-burn`, `glitch`
- 피해야: brand·emotional·minimalist — 과도하게 강함
