---
name: hyperframes-fx-flowchart
description: >-
  Flowchart — SVG 커넥터와 노드, 커서 인터랙션이 있는 결정 트리 UI 블록.
  톤: tech, brand(프로세스). 트리거: flowchart, 플로우차트, 결정 트리, decision tree,
  프로세스, 워크플로우, process flow, SVG chart.
---

# Flowchart

## 언제 쓰나
- 프로세스·결정 트리·워크플로우 설명 카드
- 여러 분기와 연결선이 있는 구조 시각화
- **톤**: tech, brand(프로세스 설명)
- **추천 duration**: 6–8초

## 설치
```bash
npx hyperframes add flowchart
```
→ `compositions/flowchart.html`.

## 와이어링
```html
<div data-composition-src="compositions/flowchart.html"
     data-start="10" data-duration="6"
     data-track-index="0"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 노드·엣지·레이아웃은 블록 내부 SVG에서 편집

## 짝
- 잘 맞음: `cinematic-zoom`으로 진입 (줌인으로 플로우에 집중)
- 피해야: `glitch`, `destruction` — 구조가 흐트러짐
