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

AI 뉴스의 신규 표지·대표 이미지는 `hyperframes-card-news-fomo-image-direction`을 먼저 적용해 사실 확인, 주인공, 시각적 은유, A/B/C 시안을 정한 뒤 이 스킬로 구현한다.

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

## FOMO 이미지 선택 규칙

- 한 장에 **주인공 하나, 기사 고유 사물 하나, 시각적 은유 하나**만 둔다.
- 얼굴·제품·스마트폰·공식 UI처럼 1초 안에 식별되는 피사체를 상단 65-70%에 크게 배치한다.
- 가격·제한은 결제 게이트/자판기, 성능은 경주/시상대, 보안은 균열/열린 자물쇠처럼 사건을 한 장면으로 번역한다.
- `어두운 방 + 노트북 + 홀로그램 + 평범한 로봇`처럼 다른 AI 기사에도 재사용할 수 있는 generic 이미지는 거부한다.
- 공식 제품 이미지·스크린샷·사용 허가가 명확한 실사를 우선하고, 생성 이미지의 글자·숫자·로고·UI는 믿지 않는다.
- 로고, 가격, 날짜, 제품명은 모델이 아니라 HTML/CSS에서 정확히 합성한다.
- 실존 인물이나 실제 사건을 AI로 가짜 현장 사진처럼 만들지 않는다. 불가피한 생성·연출 이미지는 카드 또는 캡션에 표시한다.
- 축소 피드에서 주인공이 보이는 A/B/C 시안 중 하나를 선택한다. 선택 기준은 `hyperframes-card-news-fomo-image-direction`을 따른다.

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
- [ ] AI 뉴스 표지면 `hyperframes-card-news-fomo-image-direction`을 함께 적용
- [ ] 텍스트를 가려도 기사 주제 또는 사건 방향이 읽힘
- [ ] 주인공 하나·기사 고유 사물 하나·은유 하나로 정리됨
- [ ] generic AI 작업실·로봇·홀로그램 이미지를 사용하지 않음
- [ ] 브랜드/출처 핸들이 검정 박스 위에 있음
- [ ] 하단 카피 영역이 충분히 어두움
- [ ] 사진은 `assets/` 상대경로
- [ ] 생성·연출 이미지의 오해 방지 표시를 확인함
- [ ] 일반 텍스트 설명 카드처럼 쓰지 않음
