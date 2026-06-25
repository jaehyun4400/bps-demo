# ⚔️ Blades of Plumflower Beneath Snow (BPS)

> **가상의 모바일 라이브 수집형 RPG(v1.2 → v1.3 업데이트)를 대상으로 한 플레이어블 QA 포트폴리오**
> — 모바일 게임 서비스 QA 관점으로 설계·검증한 인터랙티브 프로젝트 (Web 기반 · Mobile-first)

[![QA Portfolio](https://img.shields.io/badge/Mobile%20Game-QA%20Portfolio-blueviolet)](./qa)
[![Playable Prototype](https://img.shields.io/badge/Playable-Prototype-orange)](./index.html)
[![라이브 데모](https://img.shields.io/badge/Live-Demo-brightgreen)](https://jaehyun4400.github.io/bps-demo/)

> 💡 **이 프로젝트의 정체성**: "웹게임을 만든 것"이 아니라, 실제 모바일 라이브 게임 QA를 가정하고
> **게임 설계 → 업데이트(v1.2→v1.3) → 테스트 전략 → 결함 검증 → 추적성 → 회고**를 한 세트로 보여주는 QA 산출물입니다.
> 웹은 "실제로 만져볼 수 있는 검증 환경"을 제공하기 위한 구현 수단입니다.

---

## 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 목적 | 모바일 게임 서비스 QA 역량 증빙 — 게임 설계 / 테스트 전략 / 결함 검증 / 추적성 / 회고를 한 세트로 제시 |
| QA 산출물 | TEST_PLAN · TEST_CASES · BUG_REPORT · TRACEABILITY · TEST_REPORT (+ [회고](./qa/RETROSPECTIVE.md)) |
| 검증 방식 | 의도적 결함(planted bug) 매설 → 재현 → 영향도 분석, Playwright 자동화 시뮬레이션 |
| 게임 장르 | 동양 궁중 판타지 모바일 수집형 방치 RPG (가상 · Android / iOS) |
| 검증 환경 | 플레이어블 프로토타입 — 세로형 모바일 뷰(390×844), 바닐라 HTML/CSS/JS 단일 파일(약 3,450줄, 외부 라이브러리 0개), 서버 없이 브라우저 실행 |

---

## QA 산출물

v1.2.0 · v1.3.0 업데이트를 대상으로 작성된 QA 문서입니다. **버전별로 `qa/1.2/`, `qa/1.3/` 폴더에 완전 분리**하여 관리합니다 (각 폴더 내 TC/Bug ID는 폴더 단독 번호 체계 — 버전 간 동일 번호가 다른 항목을 가리킬 수 있으니 폴더 경로로 구분).

| 버전 | 문서 |
|---|---|
| **v1.2.0** | [TEST_PLAN](./qa/1.2/TEST_PLAN.md) · [TEST_CASES](./qa/1.2/TEST_CASES.md) (38개) · [BUG_REPORT](./qa/1.2/BUG_REPORT.md) (BUG-001~002) · [TRACEABILITY](./qa/1.2/TRACEABILITY.md) · [TEST_REPORT](./qa/1.2/TEST_REPORT.md) |
| **v1.3.0** | [TEST_PLAN](./qa/1.3/TEST_PLAN.md) · [TEST_CASES](./qa/1.3/TEST_CASES.md) (17개) · [BUG_REPORT](./qa/1.3/BUG_REPORT.md) (BUG-001~002) · [TRACEABILITY](./qa/1.3/TRACEABILITY.md) · [TEST_REPORT](./qa/1.3/TEST_REPORT.md) |

### 테스트 결과 요약

| 항목 | v1.2.0 (`qa/1.2/`) | v1.3.0 (`qa/1.3/`) |
|---|---|---|
| 총 TC | 38 | 17 |
| PASS | 36 (94.7%) | 15 (88.2%) |
| FAIL | 2 | 2 |
| 미해결 결함 | BUG-001 Critical / BUG-002 Major | BUG-001 Major / BUG-002 Major |
| 출시 권고 | **보류** (BUG-001 수정 후 재검증) | **보류** (BUG-001·002 수정 후 재검증) |

---

## 기술 문서

| 문서 | 설명 |
|---|---|
| [GAME_SPEC.md](./docs/GAME_SPEC.md) | 게임 스펙 (v1.3.0) — 캐릭터, 몬스터, 던전, 아이템, 소환, 라이브 콘텐츠, 업적 |
| [ReleaseNote.md](./docs/ReleaseNote.md) | 릴리즈 노트 (~v1.3.0) |
| [RETROSPECTIVE.md](./qa/RETROSPECTIVE.md) | **QA 회고** — 테스트 범위 정의, 실서비스라면 추가했을 검증, 다음 개선 계획 |
| [BPS_devlog.md](./BPS_devlog/BPS_devlog.md) | 구현 개발 일지 (Phase 1~7) |

---

## 라이브 데모

**[▶ 지금 플레이하기](https://jaehyun4400.github.io/bps-demo/)**

- 타이틀 → 로비 → 던전 → 전투 플레이 가능
- 편성 / 성장 / 소환 / 픽업 배너 / 이벤트 / 상점 / 우편 / 업적 / 출석 / 리딤코드 포함
- 리딤코드 `POWERPOWER` 입력 시 무제한 자원으로 전 시스템 테스트 가능

---

*© 2026 jaehyun4400 — QA Portfolio Project*
