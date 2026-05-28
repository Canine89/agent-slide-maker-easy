# lab-hyperframes

HyperFrames 기반 슬라이드·영상 실험장. 주제별로 독립된 서브프로젝트를 `topics/` 아래 둔다.

## 폴더 구조

```
lab-hyperframes/
├── .claude/skills                Claude Code용 스킬 심링크
├── .codex/skills/                Codex용 로컬 스킬 원본
├── .cursor/skills                Cursor용 스킬 심링크
├── AGENTS.md, CLAUDE.md          에이전트 가이드
├── PROJECT.md                    이 문서
├── hyperframes.json, meta.json   워크스페이스 마커
│
├── topics/                       주제별 서브프로젝트
│   ├── _template/                새 주제 시작용 뼈대
│   ├── openai-history/           OpenAI 역사 10장
│   └── <주제 이름>/               각 주제 디렉토리
│       ├── hyperframes.json      (필수)
│       ├── meta.json             (필수 — name이 렌더 파일명에 반영됨)
│       ├── index.html            영상 소스 (GSAP 타임라인)
│       ├── static.html           정적 HTML 덱 (애니메이션 없음)
│       ├── assets/               주제 전용 이미지·폰트
│       ├── renders/              mp4 결과물
│       └── snapshots/            PNG 스냅샷
│
└── _archive/                     과거 테스트 산출물
```

## 새 주제 만들기

```bash
# 1. 템플릿 복사
cp -r topics/_template topics/<주제-이름>

# 2. meta.json 의 name 교체
# topics/<주제-이름>/meta.json 파일을 열어서
# "id" 와 "name" 을 <주제-이름>으로 변경

# 3. index.html 작성 (에이전트에게 맡기는 경우)
# "사주팔자 10장짜리 슬라이드 만들어줘" 처럼 지시
# 에이전트는 .codex/skills/hyperframes-slide-work-* 스킬을 참조해
# topics/<주제-이름>/index.html 을 작성
```

## Preview (live 브라우저 미리보기)

```bash
npx hyperframes preview topics/<주제-이름>
```

## Render (mp4 생성)

```bash
npx hyperframes render topics/<주제-이름>
# → topics/<주제-이름>/renders/<주제-이름>_<timestamp>.mp4 생성
```

## Snapshot (PNG 정지 이미지 뽑기)

```bash
# 씬별 peak 타임스탬프 지정
npx hyperframes snapshot topics/<주제-이름> --at 2.5,8.1,13.7,...
# → topics/<주제-이름>/snapshots/frame-*.png
```

## Static HTML 덱 (정지 버전)

`topics/<주제-이름>/static.html` 에 애니메이션 없는 순수 HTML 덱을 작성.
브라우저에서 열어 바로 보거나, "PDF로 저장" 으로 16:9 10페이지 PDF 덱 생성 가능.

## Lint (컴포지션 검증)

```bash
npx hyperframes lint topics/<주제-이름>
```

## 슬라이드 타입 10종 스킬

`.codex/skills/hyperframes-slide-work-*` 에 각 슬라이드 타입별 SKILL.md 가 있다.
에이전트가 자동 트리거한다.

| 스킬 | 용도 |
|---|---|
| `title` | 표지·섹션 구분·마무리 |
| `title-bullets` | 설명형 기본 |
| `title-image` | 제목 + 대표 이미지 |
| `title-tags` | 키워드 나열 |
| `split` | 이미지 + 불릿 좌우 분할 |
| `quote` | 인용문 중앙 정렬 |
| `stat` | 숫자·KPI 강조 |
| `steps` | 번호 있는 순차 단계 |
| `compare` | 2~4개 항목 병렬 비교 |
| `evolution-flow` | before → after 흐름 |

## 참고

- HyperFrames 문서: https://hyperframes.heygen.com
- GSAP 애니메이션: https://greensock.com/docs/
- 10슬라이드 × 6초 × 0.4초 오버랩 = 약 56초가 기본 페이싱
- 씬은 `.scene.clip` 클래스 필수, 트랙(`data-track-index`)은 0/1 번갈아 씀
- 모든 씬은 entrance-only, exit 애니메이션은 마지막 씬에서만 허용
