---
name: hyperframes-fx-gravitational-lens
description: >-
  Gravitational Lens — 중력 렌즈 왜곡 트랜지션. 공간이 휘어지는 SF 감성.
  톤: tech. 트리거: 중력, 공간 왜곡, 렌즈, sci-fi, SF 전환, 물리 효과, 블랙홀, 워프.
---

# Gravitational Lens

## 언제 쓰나
- SF·우주·물리·AI 같은 테크/사이언스 테마
- "현실이 휘어진다" 같은 메타포 전환
- **톤**: tech (SF 감성)
- **추천 duration**: 0.6–0.9초

## 설치
```bash
npx hyperframes add gravitational-lens
```
→ `compositions/gravitational-lens.html`.

## 와이어링
```html
<div data-composition-src="compositions/gravitational-lens.html"
     data-start="4.5" data-duration="0.8"
     data-track-index="1"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 렌즈 강도·중심점·왜곡 범위는 shader 내부

## 짝
- 잘 맞음: `sdf-iris`, `cinematic-zoom`, `chromatic-radial-split`
- 피해야: brand·emotional — SF 톤이 강해 브랜드 메시지 약화
