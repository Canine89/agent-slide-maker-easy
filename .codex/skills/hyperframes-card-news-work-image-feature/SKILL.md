---
name: hyperframes-card-news-work-image-feature
description: >-
  HyperFrames 인스타 카드뉴스의 image-feature 카드 전용 작업 스킬. 이미지 또는
  포스터를 중심에 두고 블러/그라디언트 배경, 큰 헤드라인, 2-3개 짧은 문단으로
  맥락을 설명하는 카드 작업에 사용. hyperframes-card-news의 4개 허용 템플릿 중
  image-feature의 소스 오브 트루스.
---

# Card News Work: Image Feature

## 역할

`image-feature`는 이미지가 스토리의 중심일 때 쓰는 설명형 카드다. 사진·제품 컷·포스터·스크린샷을 먼저 보여주고, 아래에 헤드라인과 짧은 본문을 붙인다.

허용 클래스:

```html
<div id="c-N" class="card clip image-feature"
     data-start="..." data-duration="5" data-track-index="0">
```

## 구조

```html
<div id="c-N" class="card clip image-feature"
     data-start="15" data-duration="5" data-track-index="0">
  <div class="feature-bg" aria-hidden="true"
       style="background-image: url('assets/featured.jpg');"></div>
  <div class="feature-content">
    <div class="feature-frame">
      <img src="assets/featured.jpg" alt="설명" />
    </div>
    <div class="feature-headline">이미지가 전하는 메시지 한 줄</div>
    <div class="feature-body">
      <p>본문 첫 번째 단락.</p>
      <p>본문 두 번째 단락.</p>
    </div>
  </div>
  <div class="page-indicator">04 · 08</div>
</div>
```

## 내용 규칙

- 이미지가 반드시 있어야 한다. 이미지 없이 텍스트 카드로 쓰지 않는다.
- 헤드라인은 1개, 1-2줄.
- 본문은 2-3개 `<p>`, 각 문단 1문장 중심.
- 긴 연대기·복수 불릿은 여러 카드로 나눈다.

## CSS 규칙

```css
.card.image-feature {
  padding: 0;
  overflow: hidden;
}
.image-feature .feature-bg {
  position: absolute;
  inset: -40px;
  z-index: 0;
  background-size: cover;
  background-position: center;
  filter: blur(48px) brightness(0.45);
  transform: scale(1.12);
}
.image-feature .feature-content {
  position: relative;
  z-index: 1;
  height: 100%;
  padding: 88px 72px 112px;
  display: flex;
  flex-direction: column;
}
.image-feature .feature-frame {
  width: 100%;
  height: 420-620px;
  border-radius: 12-28px;
  overflow: hidden;
}
.image-feature .feature-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.image-feature .feature-headline {
  margin-top: 48-64px;
  font-size: 56-76px;
  font-weight: 700-850;
  line-height: 1.06-1.25;
}
.image-feature .feature-body p {
  font-size: 28-32px;
  line-height: 1.40-1.55;
}
```

## 배경 이미지 규칙

- 블러 배경은 CSS `background-image`로 넣는다.
- 같은 이미지를 `<img>`로도 쓰면 린터가 `duplicate_media_discovery_risk` 경고를 낼 수 있다. 경고를 줄이려면 배경은 그라디언트나 색면으로 대체한다.
- 어두운 카드에서는 `brightness(0.45)`, 밝은 Apple식 카드에서는 `brightness(1.08) saturate(0.88); opacity: 0.30`처럼 조정 가능.

## GSAP

```js
tl.from("#c-N .feature-bg", { scale: 1.18, duration: 1.1, ease: "power2.out" }, s);
tl.from("#c-N .feature-frame", { y: 26, opacity: 0, duration: 0.75, ease: "power3.out" }, s + 0.35);
tl.from("#c-N .feature-headline", { y: 26, opacity: 0, duration: 0.75, ease: "expo.out" }, s + 0.95);
tl.from("#c-N .feature-body p", { y: 16, opacity: 0, duration: 0.55, ease: "power2.out", stagger: 0.12 }, s + 1.35);
tl.from("#c-N .page-indicator", { opacity: 0, duration: 0.4, ease: "power2.out" }, s + 2.0);
```

## 체크

- [ ] `data-skill="image-feature"`로 overview에 기록
- [ ] 이미지 또는 시각 프레임이 있음
- [ ] 헤드라인 1개, 본문 2-3문단
- [ ] 텍스트 전용 설명 카드로 변질되지 않음
