---
name: hyperframes-fx-grid-pixelate-wipe
description: >-
  Grid Pixelate Wipe — 화면이 그리드 타일로 쪼개져 스태거 페이드 아웃되는 지속형
  컴포넌트 전환. 톤: tech, minimalist. 트리거: pixelate, 픽셀, 그리드 와이프,
  mosaic, 타일 디졸브, 8bit transition.
---

# Grid Pixelate Wipe

## 언제 쓰나
- 테크·데이터 카드의 "디지털" 리빌
- 8비트·레트로 게임 감성
- **톤**: tech, minimalist
- **피해야**: emotional, 감성 톤

## 설치
```bash
npx hyperframes add grid-pixelate-wipe
```
→ `compositions/components/grid-pixelate-wipe.html` 생성.

## 와이어링 (컴포넌트 방식)

`components/grid-pixelate-wipe.html` 의 HTML/CSS 스니펫을 복사해 씬 사이에 삽입. 자체적으로 키프레임을 돌리므로 data-* 타이밍만 맞춰주면 됨.

```html
<div class="grid-pixelate-wipe"
     data-start="4.6" data-duration="0.6"
     data-track-index="1"
     style="position: absolute; inset: 0;">
  <!-- grid-pixelate-wipe.html의 스니펫 -->
</div>
```

## 파라미터
- 타일 개수·스태거 지연은 CSS custom properties로 조정 (컴포넌트 내부)

## 짝
- 잘 맞음: `transitions-grid`, `chromatic-radial-split`
- 피해야: `light-leak`, `grain-overlay` — 디지털 vs 아날로그 충돌
