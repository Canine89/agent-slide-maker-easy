---
name: hyperframes-slide-work-kindergarten-notice
description: >-
  HyperFrames 컴포지션에서 유치원·어린이집 교사가 학부모에게 보내는 알림장,
  놀이 기록, 주간 교육 안내 스타일의 16:9 슬라이드를 만들 때 사용. 노란 격자
  배경, 데이지·벌 장식, 둥근 구름형 패널, 점선 테두리, 원형/육각형 사진 마스크,
  큰 한글 제목과 교사 관찰문 중심의 유아교육용 안내 슬라이드 패턴.
---

# Kindergarten Parent Notice Slides

## 언제 쓰나

- 유치원·어린이집 학부모 안내, 놀이 기록, 프로젝트 활동 공유, 다음 놀이 예고 슬라이드
- 교사가 찍은 교실·바깥놀이 사진과 관찰 문장을 부드럽고 신뢰감 있게 보여줄 때
- 참고 스타일: 연노랑 격자 배경, 흰 데이지, 작은 벌, 크림색 구름/가리비 패널, 주황 라벨, 진파랑 대제목

## 기본 미감

- **배경**: `#FBE987` 계열 노랑 + 64px 내외 흰 격자. 너무 진한 노랑 금지.
- **주색**: 진파랑 `#006FB4`, 주황 `#FDB515`, 크림 `#FFF7CE`, 흰 패널.
- **폰트**: Paperlogy 우선. 제목 800-900, 본문 700 이상. 유아교육 알림은 한글 가독성이 우선이다.
- **장식**: 데이지와 벌은 CSS/SVG로 만든다. 랜덤 배치 금지, 슬라이드별 2-5개만.
- **사진**: 실제 사진이 있으면 `assets/` 상대경로. 없으면 `.photo.placeholder`로 따뜻한 교육 현장 느낌의 패턴만 둔다.
- **텍스트**: 학부모에게 보여주는 문장은 설명문보다 관찰 기록 톤. “아이들이 ~했습니다”, “관심을 보였습니다”처럼 쓴다.

## 레이아웃 원형

| 타입 | 쓰임 | 구조 |
| --- | --- | --- |
| `bee-cover` | 표지 | 곡선 상단 제목 + 큰 구름 패널 + 기간 라벨 + 꽃밭 장식 |
| `notice-story` | 놀이의 시작 | 중앙 흰 점선 패널 + 큰 본문 + 2-3개 원형 사진 |
| `hex-gallery` | 세부 활동 정리 | 왼쪽 설명 리스트 + 오른쪽 육각형 사진 클러스터 |
| `teacher-note` | 긴 관찰 기록 | 상단 사진 띠 + 본문 2단락 + 밑줄 강조 |
| `next-play` | 다음 놀이 예고 | 3열 카드, 각 카드에 라벨·사진·교사 지원계획 |

## HTML 구조

모든 씬은 1920×1080, `clip`과 타이밍 속성을 포함한다.

```html
<div id="s-2" class="scene clip notice-story"
     data-start="6" data-duration="6" data-track-index="0">
  <div class="pill-title">놀이의 시작</div>
  <section class="paper-panel">
    <p class="story-text">아이들은 바깥놀이에서 ... 관심을 보였습니다.</p>
  </section>
  <div class="photo photo-round photo-a"><img src="assets/play-01.jpg" alt="..." /></div>
  <div class="bee bee-bottom" aria-hidden="true"></div>
</div>
```

## CSS 필수 블록

- `html, body`에 Paperlogy CDN과 font stack 적용.
- `.scene`에 노란 격자 배경:

```css
.scene {
  width: 1920px; height: 1080px; position: relative; overflow: hidden;
  background-color: #FBE987;
  background-image:
    linear-gradient(rgba(255,255,255,.78) 2px, transparent 2px),
    linear-gradient(90deg, rgba(255,255,255,.78) 2px, transparent 2px);
  background-size: 64px 64px;
  color: #111827;
  font-family: "Paperlogy", "Inter", "Helvetica Neue", Arial, sans-serif;
  word-break: keep-all;
}
```

- 패널은 점선 테두리와 큰 radius:

```css
.paper-panel {
  background: #fff;
  border: 5px dashed #F6C65B;
  border-radius: 28px;
  box-shadow: 0 10px 0 rgba(255, 181, 21, .18);
}
```

- 구름 표지는 `border-radius: 50%` 원 여러 개를 겹치거나 `clip-path` 대신 안정적인 pseudo-element를 사용한다.
- 육각 사진은 `clip-path: polygon(25% 5%, 75% 5%, 100% 50%, 75% 95%, 25% 95%, 0 50%)`.
- 꽃과 벌은 `.daisy`, `.bee` 공통 클래스로 만들고 `aria-hidden="true"`를 붙인다.

## GSAP 엔트런스

```js
const tl = gsap.timeline({ paused: true });
tl.from("#s-2 .pill-title", { y: -28, opacity: 0, duration: 0.55, ease: "back.out(1.8)" }, start + 0.2);
tl.from("#s-2 .paper-panel", { y: 32, opacity: 0, duration: 0.7, ease: "power3.out" }, start + 0.45);
tl.from("#s-2 .photo", { scale: 0.82, opacity: 0, duration: 0.65, stagger: 0.12, ease: "back.out(1.7)" }, start + 0.8);
tl.from("#s-2 .story-text", { y: 18, opacity: 0, duration: 0.65, ease: "power2.out" }, start + 1.05);
window.__timelines["main"] = tl;
```

## 작성 원칙

- 한 슬라이드의 본문은 4-8줄. 학부모 알림장 톤에서는 너무 압축하지 않는다.
- 숫자 목록은 `1.`, `2.`처럼 짧게. 긴 설명은 다음 슬라이드로 분리한다.
- 사진이 많아도 한 슬라이드 4장 이하. 사진은 원형·둥근 사각형·육각형 중 하나의 규칙으로 통일한다.
- 화면 하단 꽃밭 장식은 본문 영역과 겹치지 않게 `bottom: -8px` 근처에 고정한다.
- `overview.html`을 만들 때는 반드시 `hyperframes-overview-edit`의 Edit 버튼 기능을 포함한다.

## 검증

작업 후:

```bash
npx hyperframes lint topics/<주제>
bash .codex/skills/hyperframes-overview/serve.sh topics/<주제> 8765
```

사용자에게 먼저 `overview.html` URL을 제시한다. 영상 렌더는 사용자가 오버뷰 OK 후 명시적으로 요청할 때만 실행한다.
