---
name: hyperframes-fx-grain-overlay
description: >-
  Grain Overlay — 필름 그레인 질감의 지속형 오버레이 컴포넌트. 덱 전체에 얇게
  깔면 매거진·시네마 무드 통일. 톤: brand, news, emotional. 트리거: grain, 그레인,
  필름 질감, 노이즈, 질감 오버레이, 빈티지 질감, analog texture.
---

# Grain Overlay

## 언제 쓰나
- 모든 카드 위에 얇게(3–5% opacity) 깔아 매거진/시네마 무드
- brand·news·emotional 톤에 통일감 부여
- **톤**: brand, news, emotional
- **피해야**: tech·minimalist — 깨끗한 화면 방해

## 설치
```bash
npx hyperframes add grain-overlay
```
→ `compositions/components/grain-overlay.html` 생성.

## 와이어링 (컴포넌트 방식)

Shader transition과 달리 **HTML/CSS 스니펫을 직접 삽입**한다. `compositions/components/grain-overlay.html` 파일 안의 스니펫을 복사해 각 카드 안에 또는 `#root` 직하위에 붙인다.

```html
<!-- 모든 카드 위에 전 시간 동안 깔리는 오버레이 -->
<div class="grain-overlay"
     data-start="0" data-duration="20"
     data-track-index="2"
     style="position: absolute; inset: 0; z-index: 100; pointer-events: none; opacity: 0.04;">
  <!-- grain-overlay.html의 CSS keyframes + <div> 구조 복사 -->
</div>
```

## 파라미터
- opacity 조정: brand 0.03, news 0.05, emotional 0.04 권장
- animation speed / grain size는 CSS keyframes 내부

## 짝
- 잘 맞음: `light-leak`, `shimmer-sweep`, 모든 shader transition
- 한 덱에 1개만 — 중복 금지
