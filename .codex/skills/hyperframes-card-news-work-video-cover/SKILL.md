---
name: hyperframes-card-news-work-video-cover
description: >-
  HyperFrames 인스타 카드뉴스의 video-cover 카드 전용 작업 스킬. 짧은 무음
  동영상을 stage 직하위 timed media로 깔고, 별도 오버레이 카드에 하단 블랙
  그라디언트와 대형 헤드라인을 얹는 오프닝 카드 작업에 사용. hyperframes-card-news의
  4개 허용 템플릿 중 video-cover의 소스 오브 트루스.
---

# Card News Work: Video Cover

## 역할

`video-cover`는 실제 장소·현장·제품·인터페이스가 움직이는 장면으로 여는 카드다. `photo-cover`와 목표는 같지만 배경이 이미지가 아니라 짧은 무음 동영상이다.

## 필수 구조

HyperFrames 렌더러 제약 때문에 `<video>`를 timed 카드 내부에 넣지 않는다. 영상은 stage 직하위, 텍스트/그라디언트는 별도 overlay 카드로 둔다.

```html
<video id="c-1-video" class="cover-video-media clip"
       src="assets/hook.mp4" poster="assets/hook-poster.jpg"
       data-start="0" data-duration="5" data-track-index="0"
       muted autoplay loop playsinline preload="auto"></video>

<div id="c-1" class="card clip video-cover"
     data-start="0" data-duration="5" data-track-index="1">
  <div class="video-shade" aria-hidden="true"></div>
  <div class="hook-kicker">REAL FOOTAGE</div>
  <div class="hook-title">
    <span class="line">헤드라인 첫째 줄</span>
    <span class="line">헤드라인 둘째 줄</span>
  </div>
  <div class="page-indicator">01 · 08</div>
</div>
```

## 금지

- `<div class="card clip video-cover">` 내부에 timed `<video data-start>`를 넣지 않는다.
- 영상과 overlay 카드를 같은 `data-track-index`에 두지 않는다.
- 소리 있는 비디오를 그대로 쓰지 않는다. 영상은 `muted`; 오디오가 필요하면 별도 `<audio>` 규칙을 따른다.

## CSS 규칙

```css
.cover-video-media {
  position: absolute;
  top: 0;
  left: 0;
  width: 1080px;
  height: 1350px;
  object-fit: cover;
  z-index: 0;
}
.card.video-cover {
  padding: 0;
  background: transparent;
  z-index: 1;
}
.video-cover .video-shade {
  position: absolute;
  inset: 0;
  z-index: 1;
  background:
    linear-gradient(to bottom, rgba(0,0,0,0.12) 0%, transparent 30%),
    linear-gradient(to top, rgba(0,0,0,0.97) 0%, rgba(0,0,0,0.84) 34%, rgba(0,0,0,0.50) 62%, rgba(0,0,0,0.12) 78%, transparent 100%);
}
```

카피가 있는 하단 35%는 거의 검정에 가깝게 처리한다. 카피 위치가 하단이 아니면 그라디언트 방향을 바꾼다.

## 텍스트

- `.hook-kicker`: 현장감/브랜드/출처 라벨. 검정 박스 위에 올려도 좋다.
- `.hook-title .line`: 64-76px, weight 800-900, white, line-height 1.15-1.25.
- 2줄을 기본으로 한다. 3줄 이상은 피드에서 무겁다.

## GSAP

```js
tl.from("#c-1-video", { scale: 1.08, duration: 1.4, ease: "power2.out" }, s);
tl.from("#c-1 .hook-kicker", { y: 18, opacity: 0, duration: 0.55, ease: "power2.out" }, s + 0.7);
tl.from("#c-1 .hook-title .line", { y: 42, opacity: 0, duration: 0.75, ease: "expo.out", stagger: 0.12 }, s + 1.0);
tl.from("#c-1 .page-indicator", { opacity: 0, duration: 0.5, ease: "power2.out" }, s + 2.0);
```

## 체크

- [ ] overview에는 overlay 카드만 `data-skill="video-cover"`로 기록
- [ ] 영상은 stage 직하위 `video.cover-video-media.clip`
- [ ] 영상 track 0, overlay track 1
- [ ] `poster` 있음
- [ ] `muted autoplay loop playsinline preload="auto"` 있음
