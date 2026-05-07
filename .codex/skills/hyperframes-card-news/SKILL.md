---
name: hyperframes-card-news
description: >-
  인스타그램 카드뉴스 전용 스킬. 1:1(1080×1080) 또는 4:5(1080×1350) 모바일
  포맷으로 스와이프 카드뉴스를 HTML + GSAP으로 만들고, 정적 오버뷰와
  동일 비율 mp4 영상까지 뽑는다. 4개 템플릿(photo-cover / video-cover /
  stat / image-feature) 기반의 현대 카드뉴스 포맷. 사용자가 "인스타
  카드뉴스", "instagram card news", "피드 카드", "카드뉴스 만들어줘"
  등으로 요청할 때 사용.
---

# Instagram Card News (HyperFrames)

## 언제 쓰나

- 인스타그램 피드/캐러셀용 카드뉴스를 만들 때
- 영상(1920×1080)이 아니라 모바일 정지 이미지 + 스와이프 시뮬레이션 mp4가 필요할 때
- 10장 이하 카드에 핵심 메시지만 추려 담을 때

## 하위 템플릿 스킬 구조

이 스킬은 카드뉴스 전체 조립·토픽 생성·오버뷰·렌더 흐름을 담당한다. 개별 카드 타입의 세부 구현은 아래 4개 하위 스킬이 소스 오브 트루스다.

| 템플릿 | 하위 스킬 | 담당 |
|---|---|---|
| `photo-cover` | `hyperframes-card-news-work-photo-cover` | 전면 사진 + 브랜드/출처 검정 박스 + 하단 대형 헤드라인 |
| `video-cover` | `hyperframes-card-news-work-video-cover` | stage 직하위 영상 + overlay 카드 + 하단 대형 헤드라인 |
| `stat` | `hyperframes-card-news-work-stat` | 큰 숫자 하나 + 라벨 + 짧은 설명 |
| `image-feature` | `hyperframes-card-news-work-image-feature` | 이미지 프레임 + 블러/그라디언트 배경 + 헤드라인 + 본문 |

카드를 작성하거나 수정할 때는 해당 하위 스킬을 함께 적용한다. **이 4개 외의 카드 타입이나 `data-skill` 값은 만들지 않는다.**

기존 `hyperframes-slide-work-*` 스킬(1920×1080, 16:9)과는 완전히 다른 포맷이다. 카드뉴스는 모바일 피드에서 읽히므로:
- 폰트가 크다 (body ≥ 40px)
- 카드당 정보량이 적다 (한 카드 = 한 메시지)
- 시각 요소가 강하게 붙는다 (사진·블러 배경·대형 타이포)

## 캔버스 variant

| variant | 해상도 | 비율 | 쓰임 |
|---------|--------|------|------|
| **portrait** (기본) | 1080×1350 | 4:5 | 인스타 피드에서 가장 크게 노출. 대부분의 카드뉴스. |
| **square** | 1080×1080 | 1:1 | 클래식 인스타·프로필 어디서나 일관된 크기. |

variant 선택은 **토픽 생성 시점에 starter template을 고르는 방식**으로 결정. 런타임 스위치 없다.

- `template-portrait.html` — 4:5 기본 템플릿
- `template-square.html` — 1:1 템플릿

## 토픽 생성 흐름

```bash
# 1. 원하는 variant의 스타터를 복사
cp -r topics/_template topics/<주제-이름>
cp .codex/skills/hyperframes-card-news/template-portrait.html topics/<주제-이름>/index.html
# 또는 square:
# cp .codex/skills/hyperframes-card-news/template-square.html topics/<주제-이름>/index.html

# 2. meta.json 수정 (id / name을 <주제-이름>으로)

# 3. 4개 템플릿(photo-cover / video-cover / stat / image-feature)을 조합해 카드 구성
#    각 카드 구현은 hyperframes-card-news-work-* 하위 스킬을 따른다.

# 4. 검증
npx hyperframes lint topics/<주제-이름>
```

**기존 `topics/_template/` 의 `index.html` 은 1920×1080 기준**이다. 카드뉴스를 만들 땐 반드시 덮어씌워야 한다.

## 공통 규칙

- **루트 데이터 차원**: `<div id="root" data-width="1080" data-height="1080">` (square) 또는 `data-height="1350"` (portrait)
- **`html, body, .card`** CSS 차원을 variant에 맞게 세팅 (1920×1080 금지)
- **각 카드는 `class="clip"`** + `data-start` / `data-duration` / `data-track-index` 필수
- **카드당 duration 기본 5초** (16:9 영상의 6초에서 축소 — 카드뉴스는 읽는 호흡이 짧음)
- **타임라인 등록**: `window.__timelines["main"] = gsap.timeline({ paused: true })` 필수
- **`word-break: keep-all`** 모든 텍스트 요소에 — 한글 자연 개행
- **외곽 패딩 100–120px** (1080 캔버스 기준)

## 4개 템플릿

모든 예시는 4:5 portrait(1080×1350) 기준. square는 세로 값만 1080으로 바꿔 쓴다.

| 템플릿 | 쓰임 | 특징 |
|--------|------|------|
| **photo-cover** | 표지 (사진형) | 전면 사진 + 오버레이 헤드라인. 뉴스·매거진형 후킹. |
| **video-cover** | 표지 (짧은 영상형) | 전면 짧은 무음 영상 + 하단 블랙 그라디언트 + 굵은 헤드라인. 현장감 후킹. |
| **stat** | 숫자 강조 | 큰 숫자 하나 + 라벨. |
| **image-feature** | 사진 + 본문 | 블러 배경 + 중앙 이미지 + 제목 + 3–5줄 본문. |

> 4개 모두 **영상·이미지·대형 타이포·색 블록** 중심. 전통적인 "질문 카드"나 "제목+불릿" 슬라이드 스타일은 카드뉴스 피드에서 약하게 보여서 제외.
> 세부 구현은 `hyperframes-card-news-work-photo-cover`, `hyperframes-card-news-work-video-cover`, `hyperframes-card-news-work-stat`, `hyperframes-card-news-work-image-feature` 스킬을 우선한다.

### 템플릿 선택 규칙

- 오프닝: `video-cover` 또는 `photo-cover`
- 숫자·연도·비율 중심: `stat`
- 이미지·맥락 설명 중심: `image-feature`
- 클로징: `photo-cover` 또는 `image-feature`
- 질문형 카드, 일반 제목+불릿 카드, 임의 `timeline`/`quote`/`closing` 타입은 만들지 않는다.

### 1. photo-cover — 전면 사진 후킹

한국 카드뉴스가 가장 자주 쓰는 오프닝 패턴. 전면 사진 + 하단 스크림 그라디언트 위에 굵은 헤드라인 2줄, 선택적으로 우측 상단 원형 인셋, 중간 높이에 `@핸들` 오버레이.

```html
<div id="c-1" class="card clip photo-cover"
     data-start="0" data-duration="5" data-track-index="0">
  <div class="bg-image">
    <img src="assets/hook.jpg" alt="..." />
  </div>
  <!-- 인셋은 선택 — 보조 인물·참고 이미지가 필요할 때만 -->
  <div class="inset-avatar">
    <img src="assets/inset.jpg" alt="..." />
  </div>
  <div class="hook-handle">@handle_name</div>
  <div class="hook-title">
    <span class="line">헤드라인 첫째 줄</span>
    <span class="line">헤드라인 둘째 줄</span>
  </div>
  <div class="page-indicator">01 · 04</div>
</div>
```

**CSS 핵심**
- `.card.photo-cover` — `padding: 0` (전면), `overflow: hidden`
- `.bg-image` — `position: absolute; inset: 0; z-index: 0`, `img { width: 100%; height: 100%; object-fit: cover }`
- `.inset-avatar` — `position: absolute; top: 80px; right: 80px; width: 220px; height: 220px; border-radius: 50%; overflow: hidden; border: 4px solid rgba(255,255,255,0.7)`
- `.hook-handle` — 브랜드/출처 아이덴티티 영역. 반드시 검정 박스 위에 올린다: `display: inline-flex; width: max-content; max-width: 760px; padding: 12px 18px; border-radius: 8px; background: rgba(0,0,0,0.82); box-shadow: 0 6px 18px rgba(0,0,0,0.35); color: #fff`
- `.hook-title` — `position: absolute; left: 0; right: 0; bottom: 0; padding: 260px 80px 140px; background: linear-gradient(to top, rgba(0,0,0,0.96) 0%, rgba(0,0,0,0.82) 34%, rgba(0,0,0,0.48) 64%, transparent 100%)`
- `.hook-title .line` — `display: block; font-size: 64–72px; font-weight: 800; color: #fff; line-height: 1.28`
- 카피가 있는 하단 35%는 거의 검정에 가깝게 처리한다. 사진의 원본 명도보다 텍스트 판독성을 우선한다.

**GSAP**
```js
tl.from("#c-1 .bg-image img",     { scale: 1.08, duration: 1.2, ease: "power2.out" }, s + 0.0);
tl.from("#c-1 .inset-avatar",     { scale: 0, opacity: 0, duration: 0.7, ease: "back.out(1.7)" }, s + 0.4);
tl.from("#c-1 .hook-handle",      { y: 20, opacity: 0, duration: 0.6, ease: "power2.out" }, s + 0.8);
tl.from("#c-1 .hook-title .line", { y: 40, opacity: 0, duration: 0.7, ease: "expo.out", stagger: 0.12 }, s + 1.1);
tl.from("#c-1 .page-indicator",   { opacity: 0, duration: 0.5, ease: "power2.out" }, s + 2.0);
```

**사진 소싱**: 드라마틱한 포트레이트·이벤트·제품 클로즈업이 카드뉴스에서 가장 많이 쓰임. 반드시 `assets/` 로컬 다운로드 후 상대경로 참조.

### 2. video-cover — 전면 짧은 영상 후킹

사용자가 준 레퍼런스처럼 실제 장소·현장·제품·인터페이스가 움직이는 장면을 카드 첫머리에 까는 오프닝 패턴. `photo-cover`와 목표는 같지만 배경이 이미지가 아니라 **짧은 무음 동영상**이다. 하단에는 검은 그라디언트를 강하게 깔고, 흰색 2줄 헤드라인을 크게 얹는다.

```html
<video id="c-2-video" class="cover-video-media clip"
       src="assets/hook.mp4" poster="assets/hook-poster.jpg"
       data-start="5" data-duration="5" data-track-index="0"
       muted autoplay loop playsinline preload="auto"></video>

<div id="c-2" class="card clip video-cover"
     data-start="5" data-duration="5" data-track-index="1">
  <div class="video-shade" aria-hidden="true"></div>
  <div class="hook-kicker">REAL FOOTAGE</div>
  <div class="hook-title">
    <span class="line">만화 아니고</span>
    <span class="line">실제 건널목 입니다</span>
  </div>
  <div class="page-indicator">02 · 04</div>
</div>
```

**CSS 핵심**
- `.cover-video-media` — `<video>`는 **카드 내부에 넣지 말고 stage 직하위**에 둔다. `position: absolute; top: 0; left: 0; width/height: canvas; object-fit: cover; z-index: 0`
- `.card.video-cover` — `padding: 0`, `background: transparent`, `overflow: hidden`, `z-index: 1`. 영상 위에 얹는 텍스트/그라디언트 오버레이 역할.
- `<video>` — 반드시 고유 `id`, `class="clip"`, `data-start`, `data-duration`, `data-track-index`, `muted autoplay loop playsinline preload="auto"` 지정. 부모 카드와 같은 start/duration을 쓴다.
- track은 분리한다. 영상은 `data-track-index="0"`, 오버레이 카드 본문은 `data-track-index="1"`을 써서 같은 트랙 겹침 오류를 피한다.
- `.video-shade` — 상단은 약하게, 하단은 강하게 어둡게 만드는 2중 그라디언트. 카피가 있는 하단 35%는 거의 검정에 가깝게 처리한다.
- `.hook-kicker` — 선택. `REAL FOOTAGE`, `LIVE SCENE`, `ON LOCATION` 같은 현장감 라벨. 필요 없으면 제거.
- `.hook-title` — `position: absolute; left: 0; right: 0; bottom: 0; padding: 0 80px 150px`
- `.hook-title .line` — 64–72px, weight 800–900, 흰색, line-height 1.2 전후, 그림자 필수
- `.page-indicator` — 흰색 70% 내외

**GSAP**
```js
tl.from("#c-2-video",             { scale: 1.08, duration: 1.4, ease: "power2.out" }, s + 0.0);
tl.from("#c-2 .hook-kicker",      { y: 18, opacity: 0, duration: 0.55, ease: "power2.out" }, s + 0.7);
tl.from("#c-2 .hook-title .line", { y: 42, opacity: 0, duration: 0.75, ease: "expo.out", stagger: 0.12 }, s + 1.0);
tl.from("#c-2 .page-indicator",   { opacity: 0, duration: 0.5, ease: "power2.out" }, s + 2.0);
```

**쓰임 팁**
- 첫 카드 또는 두 번째 카드에 사용. 특히 "이게 실제라고?" 같은 반전형 훅에 강함.
- 영상은 3–6초 루프가 가장 좋고, 오디오는 쓰지 않는다. 필요하면 별도 `<audio>` 규칙을 따른다.
- `poster` 이미지를 반드시 넣어 오버뷰·초기 로딩·정지 프레임이 비어 보이지 않게 한다.
- 영상 속 중요한 피사체가 하단 텍스트에 가리지 않도록 촬영/크롭 기준을 잡는다.
- 카피가 얹히는 방향이 하단이 아니면, 그 방향에 맞춰 그라디언트 축을 바꾼다. 예: 우측 카피면 `to left`, 좌측 카피면 `to right`.
- 어두운 밤 장면, 도시 거리, 제품 사용 장면, 화면 녹화, 현장 클립에 적합하다.

### 3. stat — 큰 숫자 하나

숫자 임팩트 카드. 지표는 **카드당 1개** (인스타에서는 여러 숫자를 나열하지 않는다).

```html
<div id="c-3" class="card clip stat-card"
     data-start="10" data-duration="5" data-track-index="0">
  <div class="eyebrow">By the Numbers</div>
  <div class="stat-num">1,000<span class="stat-unit">+</span></div>
  <div class="stat-label">전 세계 매장 수</div>
  <div class="stat-desc">30여 개국에서 운영 중 (2024 기준)</div>
  <div class="page-indicator">03 · 04</div>
</div>
```

**CSS 핵심**
- `.card.stat-card` — `justify-content: center; align-items: center; text-align: center`
- `.stat-num` — 240–280px, weight 800, line-height 1, letter-spacing 음수, `font-variant-numeric: tabular-nums`
- `.stat-unit` — 64–72px, weight 500, accent 색
- `.stat-label` — 40–44px, weight 600, margin-top 32–40px
- `.stat-desc` — 28–32px, weight 400, dim, line-height 1.45

**GSAP**
```js
tl.from("#c-3 .eyebrow",    { y: -15, opacity: 0, duration: 0.5, ease: "power3.out" }, s + 0.2);
tl.from("#c-3 .stat-num",   { scale: 0.85, opacity: 0, duration: 0.9, ease: "back.out(1.6)" }, s + 0.5);
tl.from("#c-3 .stat-label", { y: 20, opacity: 0, duration: 0.6, ease: "power2.out" }, s + 1.3);
tl.from("#c-3 .stat-desc",  { opacity: 0, duration: 0.6, ease: "power2.out" }, s + 1.6);
```

### 4. image-feature — 블러 배경 + 중앙 이미지 + 본문

이미지에 대한 설명을 길게 풀 때 쓰는 스토리형 템플릿. 같은 이미지를 크게 블러/어둡게 깔고, 그 위에 오리지널 이미지를 깔끔하게 얹은 뒤 아래에 헤드라인 + 3–5줄 본문을 배치한다.

```html
<div id="c-4" class="card clip image-feature"
     data-start="15" data-duration="5" data-track-index="0">
  <div class="feature-bg" aria-hidden="true"
       style="background-image: url('assets/featured.jpg');"></div>
  <div class="feature-content">
    <div class="feature-frame">
      <img src="assets/featured.jpg" alt="설명" />
    </div>
    <div class="feature-headline">이미지가 전하는 메시지 한 줄</div>
    <div class="feature-body">
      <p>본문 첫 번째 단락 — 배경, 맥락, 사건을 간결히.</p>
      <p>본문 두 번째 단락 — 부연 설명 또는 결과를 한두 문장.</p>
    </div>
  </div>
  <div class="page-indicator">04 · 04</div>
</div>
```

> 블러 배경은 **CSS `background-image`** 로 로드한다. `<img>` 태그를 이중으로 넣으면 린터가 `duplicate_media_discovery_risk` 경고를 낸다.

**CSS 핵심**
- `.card.image-feature` — dark bg (`#0b0d10` 등), `padding: 0`, `overflow: hidden`
- `.feature-bg` — `position: absolute; inset: -40px; z-index: 0; background-size: cover; background-position: center; filter: blur(48px) brightness(0.45); transform: scale(1.12)` — 같은 이미지를 CSS bg로 크게 블러
- `.feature-content` — `position: relative; z-index: 1; padding: 96px 80px; display: flex; flex-direction: column; align-items: center; height: 100%`
- `.feature-frame` — `width: 78%; aspect-ratio: 1/1; border-radius: 12px; overflow: hidden; box-shadow: 0 12px 32px rgba(0,0,0,0.45)`
- `.feature-headline` — 56–64px, weight 700, color `#fff`, line-height 1.25, margin-top 56px
- `.feature-body p` — 28–32px, weight 400, line-height 1.55, color `rgba(255,255,255,0.82)`
- `.feature-body p + p` — `margin-top: 16px`

**GSAP**
```js
tl.from("#c-4 .feature-bg",       { scale: 1.22, duration: 1.2, ease: "power2.out" }, s + 0.0);
tl.from("#c-4 .feature-frame",    { scale: 0.9, opacity: 0, duration: 0.9, ease: "power3.out" }, s + 0.3);
tl.from("#c-4 .feature-headline", { y: 24, opacity: 0, duration: 0.7, ease: "expo.out" }, s + 1.0);
tl.from("#c-4 .feature-body p",   { y: 16, opacity: 0, duration: 0.6, ease: "power2.out", stagger: 0.12 }, s + 1.4);
tl.from("#c-4 .page-indicator",   { opacity: 0, duration: 0.5, ease: "power2.out" }, s + 2.1);
```

**사용 팁**
- 이미지가 스토리의 중심일 때 (사람·장소·물건을 보여주며 설명)
- 본문은 2–3단락 내, 각 단락 1–2문장
- 같은 이미지를 배경·프레임 양쪽에 쓰는 게 기본 설계 (색감·분위기가 확장)

## 오버뷰 생성

`overview-template.html` 을 복사해서 카드 내용을 채우면 된다. 이미 `--canvas-w`, `--canvas-h`, `--card-aspect` CSS 변수로 파라미터화돼 있다.

> **필수 참조**: overview.html 은 **반드시 `hyperframes-overview-edit` 스킬의 Edit 기능을 포함**해야 한다. 새로 생성하든 기존 파일을 수정하든, Edit 버튼 + CSS + JS(카드뉴스는 `js-card.html` variant) 가 누락되지 않도록 해당 스킬을 참조해 체크한다. 검증 커맨드: `grep -L "class=\"edit-btn\"" topics/*/overview.html`.

### 썸네일·내보내기 필수 규칙

좌측 스트립 썸네일은 반드시 유지한다. 단, 썸네일은 별도 디자인이 아니라 우측 디테일 카드 DOM을 축소한 미리보기여야 한다.

- 썸네일은 `card.cloneNode(true)` 로 만들고, `.thumb .card { display: flex; transform: scale(...); }` 를 명시한다. 우측 `.detail-frame .card.active { display: flex; }` 와 같은 display 모델이어야 축소 썸네일과 편집 화면 레이아웃이 일치한다.
- 썸네일 라벨(`.thumb-label`)은 카드 내용을 가리지 않게 기본 숨김, hover 때만 표시한다.
- Edit → Done 후에는 변경된 카드 번호에 대해 `syncThumbFromCard(n)` 로 오른쪽 최신 DOM을 다시 clone 해서 좌측 썸네일을 즉시 갱신한다.
- PDF/print/export 는 좌측 strip 기준이 아니라 우측 `#detail-frame` 안의 원본 카드 기준이어야 한다. `@media print` 에서 `.strip`, `.main-header`, Aim/Edit UI를 숨기고, `.detail-frame .card` 전체를 카드 크기별 페이지 단위로 출력한다.
- 이 규칙은 샘플뿐 아니라 새로 생성하는 모든 카드뉴스 overview.html 에 적용한다.

### 1. 템플릿 복사

```bash
cp .codex/skills/hyperframes-card-news/overview-template.html topics/<주제>/overview.html
```

### 2. :root 변수 교체

- **portrait**: `--canvas-w: 1080`, `--canvas-h: 1350`, `--card-aspect: 4 / 5`
- **square**:   `--canvas-w: 1080`, `--canvas-h: 1080`, `--card-aspect: 1 / 1`

### 3. 카드를 overview 구조로 변환

`index.html` 의 각 `<div id="c-N" class="card clip ..." data-start="...">` 를 overview 포맷으로:

1. `clip` 클래스 제거
2. `data-start` / `data-duration` / `data-track-index` 제거
3. `id="c-N"` 제거
4. `data-card="N"` + `data-skill="<photo-cover|video-cover|stat|image-feature>"` 추가

카드뉴스는 영상 슬라이드가 아니므로 `.brand` / `.slide-num` 같은 푸터 요소는 넣지 않는다. 카드 자체의 `.page-indicator` 가 이미 번호 역할을 한다.

```html
<div class="card photo-cover" data-card="1" data-skill="photo-cover">
  <div class="bg-image"><img src="..." /></div>
  ...
  <div class="page-indicator">01 · 04</div>
</div>
```

### 4. 서빙

이미지가 포함된 카드가 있으면 **반드시 HTTP 서버**로:

```bash
bash .codex/skills/hyperframes-overview/serve.sh topics/<주제> 8766
# → http://localhost:8766/overview.html
```

## 영상 렌더

`npx hyperframes render topics/<주제>` 그대로. 렌더러는 루트 `data-width` / `data-height` 를 그대로 읽어서:

- portrait variant → 1080×1350 mp4
- square variant → 1080×1080 mp4

카드가 4장, 각 5초 → 20초 mp4. 렌더 결과는 루트 `renders/` 또는 주제 폴더 `renders/` 에 떨어진다.

### 인스타 릴스용 9:16은?

현재 스킬은 지원하지 않는다. 카드뉴스와 릴스는 제작 흐름이 다르므로 별도 스킬로 분리하는 것을 권한다.

## 작성 원칙

- **한 카드 = 한 메시지**. 두 개 이상 메시지가 들어가면 카드를 쪼갠다.
- **시각 요소 필수** — 4개 템플릿 모두 이미지 또는 대형 타이포가 카드의 주인공. 일반 텍스트 문단 나열은 안 어울린다.
- **첫 카드는 photo-cover 또는 video-cover**. 피드에서 스크롤을 멈추게 하려면 강한 정지 이미지나 실제 움직임이 필요.
- **카드 3–7장 권장**. 너무 적으면 호흡이 짧고, 너무 많으면 이탈률↑.
- **마지막 카드는 CTA 또는 요약** — `image-feature`, `photo-cover`, 로고/팔로우 계열 블록으로 마감.
- **색 팔레트는 자유**지만 고대비 필수. 피드 썸네일이 흐려 보이면 실패.

## 마크다운 감지 규칙 (생성기 연동 시)

```markdown
# [photo-cover] @handle_name
![배경](assets/hook.jpg)
![인셋](assets/inset.jpg)  # 선택
헤드라인 첫째 줄
헤드라인 둘째 줄

# [video-cover] REAL FOOTAGE
![poster](assets/hook-poster.jpg)
video: assets/hook.mp4
만화 아니고
실제 건널목 입니다

# [stat] By the Numbers
$ 1,000+
전 세계 매장 수
설명 한 줄

# [image-feature] 헤드라인
![설명](assets/featured.jpg)
본문 첫 번째 단락.
본문 두 번째 단락.
```

대괄호 안이 템플릿 타입: `photo-cover` / `video-cover` / `stat` / `image-feature`.

## 인스타 업로드 본문 캡션

카드뉴스 렌더가 끝나고 실제로 인스타에 업로드할 때 **게시물 본문(캡션)** 도 필요하다. 훅·리드·핵심 불릿·바이럴 스탯·해시태그 20개 구조의 `instagram-caption-ko.txt` 생성은 별도 스킬 **`hyperframes-instagram-caption`** 이 담당한다. 카드 내용을 기반으로 자동 작성.

## 체크리스트

생성 전:
- [ ] variant 결정 (portrait / square)
- [ ] 총 카드 수 결정 (3–7 권장)
- [ ] 각 카드의 템플릿 타입 미리 매핑 (첫 카드 = photo-cover or video-cover)

작성 중:
- [ ] 모든 카드에 `class="card clip"` + timing 속성
- [ ] `#root` 에 `data-composition-id="main"` + variant에 맞는 `data-width` / `data-height`
- [ ] `window.__timelines["main"]` 에 paused 타임라인 등록
- [ ] 이미지는 `assets/` 에 상대경로로 배치
- [ ] video-cover 영상은 `assets/` 에 mp4/webm으로 배치하고 `data-start/data-duration` + `muted autoplay loop playsinline poster` 지정
- [ ] image-feature의 배경은 CSS `background-image` (duplicate media 경고 회피)
- [ ] 한글 텍스트에 `word-break: keep-all`

완성 후:
- [ ] `npx hyperframes lint topics/<주제>` → 0 errors
- [ ] overview.html 생성 + HTTP 서버로 브라우저 확인
- [ ] `npx hyperframes render` 로 mp4 생성, 모바일에서 실제 열어보기
