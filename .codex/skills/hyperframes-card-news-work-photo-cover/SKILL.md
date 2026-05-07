---
name: hyperframes-card-news-work-photo-cover
description: >-
  HyperFrames 인스타 카드뉴스의 photo-cover 카드 전용 작업 스킬. 전면 사진,
  브랜드/출처 핸들 검정 박스, 하단 블랙 그라디언트, 2줄 대형 헤드라인으로 여는
  카드 또는 마감 카드를 만들거나 수정할 때 사용. hyperframes-card-news의 4개
  허용 템플릿 중 photo-cover의 소스 오브 트루스.
---

# Card News Work: Photo Cover

## 역할

`photo-cover`는 카드뉴스의 사진형 오프닝/클로징 카드다. 전면 사진 위에 브랜드 핸들과 2줄 헤드라인을 얹는다.

허용 클래스:

```html
<div id="c-N" class="card clip photo-cover"
     data-start="..." data-duration="5" data-track-index="0">
```

## 구조

```html
<div id="c-N" class="card clip photo-cover"
     data-start="0" data-duration="5" data-track-index="0">
  <div class="bg-image">
    <img src="assets/hook.jpg" alt="..." />
  </div>
  <div class="hook-handle">@handle_name</div>
  <div class="hook-title">
    <span class="line">헤드라인 첫째 줄</span>
    <span class="line">헤드라인 둘째 줄</span>
  </div>
  <div class="page-indicator">01 · 08</div>
</div>
```

선택 요소:
- `.inset-avatar`: 보조 인물·제품 컷이 꼭 필요할 때만 사용.

## CSS 규칙

- `.card.photo-cover`: `padding: 0`, `overflow: hidden`.
- `.bg-image`: `position: absolute; inset: 0; z-index: 0`.
- `.bg-image img`: `width: 100%; height: 100%; object-fit: cover`.
- `.hook-handle`: 브랜드/출처 아이덴티티다. 반드시 검정 박스 위에 올린다.

```css
.photo-cover .hook-handle {
  position: absolute;
  left: 72px;
  bottom: 386px;
  z-index: 3;
  display: inline-flex;
  width: max-content;
  max-width: 760px;
  padding: 12px 18px 13px;
  border-radius: 8px;
  background: rgba(0,0,0,0.82);
  box-shadow: 0 6px 18px rgba(0,0,0,0.35);
  color: #fff;
}
```

- `.hook-title`: 카피가 있는 하단 35%를 거의 검정으로 만든다. 사진 명도보다 판독성을 우선한다.

```css
.photo-cover .hook-title {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 260px 72px 142px;
  z-index: 2;
  background: linear-gradient(
    to top,
    rgba(0,0,0,0.96) 0%,
    rgba(0,0,0,0.82) 34%,
    rgba(0,0,0,0.48) 64%,
    transparent 100%
  );
}
```

- `.hook-title .line`: 64-76px, weight 800-900, white, line-height 1.15-1.28.

## GSAP

```js
tl.from("#c-N .bg-image img", { scale: 1.08, duration: 1.2, ease: "power2.out" }, s);
tl.from("#c-N .hook-handle", { y: 20, opacity: 0, duration: 0.6, ease: "power2.out" }, s + 0.7);
tl.from("#c-N .hook-title .line", { y: 40, opacity: 0, duration: 0.7, ease: "expo.out", stagger: 0.12 }, s + 1.0);
tl.from("#c-N .page-indicator", { opacity: 0, duration: 0.5, ease: "power2.out" }, s + 2.0);
```

## 체크

- [ ] `data-skill="photo-cover"`로 overview에 기록
- [ ] 브랜드/출처 핸들이 검정 박스 위에 있음
- [ ] 하단 카피 영역이 충분히 어두움
- [ ] 사진은 `assets/` 상대경로
- [ ] 일반 텍스트 설명 카드처럼 쓰지 않음
