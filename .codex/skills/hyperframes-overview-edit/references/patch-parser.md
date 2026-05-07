# Patch Parser — Overview edits 반영 절차

사용자가 대화창에 `# Overview edits — ...` 로 시작하는 마크다운을 붙여넣었을 때, agent가 index.html + overview.html 에 변경사항을 반영하는 규칙.

## 패치 포맷 (복습)

```
# Overview edits — <topic-id> (N change(s))

## Card 3 (question)
- .q-text
  OLD: 기존 텍스트 (innerHTML)
  NEW: 수정된 텍스트

## Card 5 (stat)
- .stat-label
  OLD: ...
  NEW: ...
```

16:9 슬라이드덱은 `## Slide N` 헤더.

## 파싱 규칙

1. **첫 줄**: `# Overview edits — <topic-id> (N change(s))` → `<topic-id>` 추출 → `topics/<topic-id>/` 가 작업 경로
2. **섹션 헤더**: `## Card N (skill)` 또는 `## Slide N (skill)`
   - `N` = 카드/슬라이드 번호 (1-indexed)
   - `(skill)` 은 정보용 — 반영 로직엔 영향 없음
3. **변경 항목**: `- <selector>\n  OLD: ...\n  NEW: ...`
   - `<selector>` 는 `.class-name` 형식의 단일 클래스 셀렉터 (예: `.q-text`, `.stat-label`)
   - `OLD`: innerHTML 의 trim 된 기존 값
   - `NEW`: innerHTML 의 trim 된 새 값

## 반영 대상 파일 (쌍으로 수정)

각 패치 항목을 **두 파일에 모두 반영**한다:

### 1. `topics/<topic-id>/index.html`

- 카드뉴스 (`## Card N`): `<div id="c-N"` 블록 안
- 16:9 슬라이드 (`## Slide N`): `<div id="s-N"` 블록 안
- 해당 블록 내부에서 `<... class="... <selector-class>">OLD</...>` 요소를 찾아 OLD → NEW 로 Edit

### 2. `topics/<topic-id>/overview.html`

- 카드뉴스: `<div ... data-card="N"` 블록 안
- 16:9 슬라이드: `<div ... data-slide="N"` 블록 안
- 동일 셀렉터로 요소 찾아 OLD → NEW Edit

## 구현 단계

```
1. 패치의 topic 확인 → topics/<topic>/index.html 과 overview.html 이 존재하는지 체크
2. 각 변경 항목마다:
   a. index.html 에서 Edit (카드 ID + 클래스 기준으로 유니크 매칭)
   b. overview.html 에서 Edit (data-card/data-slide + 클래스 기준)
3. 양쪽 파일 lint 돌리기 (선택) — npx hyperframes lint topics/<topic>
4. 사용자에게 요약 보고: "N건 반영, index.html·overview.html 수정 완료"
5. 렌더는 자동 실행 금지 — AGENTS.md 의 overview-first 규칙 준수
```

## 엣지 케이스

### OLD 가 파일 안에 유니크하지 않을 때

같은 클래스(`.stat-label`)가 여러 카드에 있을 수 있으므로, **Edit 의 `old_string` 은 카드 블록 앵커와 함께** 만들어야 한다. 예:

```
index.html에서 카드 3의 .stat-label을 수정할 때:

old_string:
  id="c-3" ... 안에서 (또는 인근 유니크 문맥 포함)
  <div class="stat-label">기존 텍스트</div>

new_string:
  동일 구조 + 텍스트만 교체
  <div class="stat-label">새 텍스트</div>
```

Edit 도구가 `old_string` 이 유니크해야 하므로, 카드 ID 포함한 컨텍스트를 잡아 매칭한다.

### innerHTML 에 인라인 태그가 있을 때

OLD/NEW 는 innerHTML 이므로 `<em>강조</em>` 같은 태그가 포함될 수 있다. 패치에 나온 그대로 Edit 에 전달.

### NEW 가 OLD 보다 짧아져서 잘못된 매칭 위험

드물지만, 카드 N의 OLD 가 카드 M 의 기존 NEW 후보와 우연히 같을 수 있음. **항상 카드 ID (`id="c-N"` / `data-card="N"`) 를 포함한 컨텍스트**로 old_string 을 잡아 방지.

### 패치 한 건에 여러 카드·여러 필드

순서대로 처리. 각 Edit 는 독립이므로 순서 무관. 단, **두 파일(index + overview)** 을 각 변경마다 동시에 반영해 싱크 유지.

## 사용자 보고 템플릿

```
✎ Overview 편집 반영 완료

변경 내역 (N건):
- Card 3 .q-text: "...기존..." → "...새로운..."
- Card 5 .stat-label: "..." → "..."

수정 파일:
- topics/<topic>/index.html
- topics/<topic>/overview.html

브라우저 새로고침하면 반영됩니다. 영상 렌더는 사용자 승인 후 진행합니다.
```
