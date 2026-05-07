---
name: hyperframes-fx-macos-notification
description: >-
  macOS Notification — 맥OS 시스템 알림 스타일 오버레이 UI 블록. 톤: tech, brand.
  트리거: macos, mac 알림, notification, 시스템 알림, alert, popup, toast.
---

# macOS Notification

## 언제 쓰나
- 테크 콘텐츠의 시스템 알림 재현
- brand의 "알림이 왔어요" 느낌 CTA
- **톤**: tech, brand
- **추천 duration**: 3–4초

## 설치
```bash
npx hyperframes add macos-notification
```
→ `compositions/macos-notification.html`.

## 와이어링 (카드 위에 오버레이)
```html
<div data-composition-src="compositions/macos-notification.html"
     data-start="12" data-duration="3"
     data-track-index="3"
     data-width="1080" data-height="1350">
</div>
```

## 파라미터
- 앱 아이콘·제목·본문은 블록 내부 설정

## 짝
- 잘 맞음: tech 계열 shader 트랜지션
- 피해야: `grain-overlay` — 깔끔한 OS UI 방해
