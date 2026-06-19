# ⚔️ Blades of Plumflower Beneath Snow (BPS)

> 동양 궁중 판타지 모바일 수집형 방치 RPG — QA 포트폴리오 연계 브라우저 게임 데모

[![HTML](https://img.shields.io/badge/HTML-Single%20File-orange)](./index.html)
[![JS](https://img.shields.io/badge/JavaScript-Vanilla-yellow)](./index.html)
[![라이브 데모](https://img.shields.io/badge/Live-Demo-brightgreen)](https://jaehyun4400.github.io/bps-demo/)

---

## 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 파일 | `index.html` (단일 파일, 약 3,450줄) |
| 기술 스택 | 바닐라 HTML / CSS / JavaScript (외부 라이브러리 0개) |
| 목적 | QA 포트폴리오 시각화 — 가상의 모바일 게임을 실제 플레이 가능한 데모로 구현 |
| 특이사항 | 서버 없음, 브라우저에서 직접 실행 가능 |
| 게임 장르 | 동양 궁중 판타지 모바일 수집형 방치 RPG |
| 플랫폼 (가상) | Android / iOS |

---

## QA 산출물

v1.2.0 · v1.3.0 업데이트를 대상으로 작성된 QA 문서입니다. **버전별로 `qa/1.2/`, `qa/1.3/` 폴더에 완전 분리**하여 관리합니다 (각 폴더 내 TC/Bug ID는 폴더 단독 번호 체계 — 버전 간 동일 번호가 다른 항목을 가리킬 수 있으니 폴더 경로로 구분).

| 버전 | 문서 |
|---|---|
| **v1.2.0** | [TEST_PLAN](./qa/1.2/TEST_PLAN.md) · [TEST_CASES](./qa/1.2/TEST_CASES.md) (38개) · [BUG_REPORT](./qa/1.2/BUG_REPORT.md) (BUG-001~002) · [TRACEABILITY](./qa/1.2/TRACEABILITY.md) · [TEST_REPORT](./qa/1.2/TEST_REPORT.md) |
| **v1.3.0** | [TEST_PLAN](./qa/1.3/TEST_PLAN.md) · [TEST_CASES](./qa/1.3/TEST_CASES.md) (13개) · [BUG_REPORT](./qa/1.3/BUG_REPORT.md) (BUG-001~002) · [TRACEABILITY](./qa/1.3/TRACEABILITY.md) · [TEST_REPORT](./qa/1.3/TEST_REPORT.md) |

### 테스트 결과 요약

| 항목 | v1.2.0 (`qa/1.2/`) | v1.3.0 (`qa/1.3/`) |
|---|---|---|
| 총 TC | 38 | 13 |
| PASS | 36 (94.7%) | 11 (84.6%) |
| FAIL | 2 | 2 |
| 미해결 결함 | BUG-001 Critical / BUG-002 Major | BUG-001 Major / BUG-002 Major |
| 출시 권고 | **보류** (BUG-001 수정 후 재검증) | **보류** (BUG-001·002 수정 후 재검증) |

---

## 기술 문서

| 문서 | 설명 |
|---|---|
| [GAME_SPEC.md](./docs/GAME_SPEC.md) | 게임 스펙 (v1.3.0) — 캐릭터, 몬스터, 던전, 아이템, 소환, 라이브 콘텐츠, 업적 |
| [ReleaseNote.md](./docs/ReleaseNote.md) | 릴리즈 노트 (~v1.3.0) |
| [BPS_devlog.md](./BPS_devlog/BPS_devlog.md) | 구현 개발 일지 (Phase 1~7) |

---

## 라이브 데모

**[▶ 지금 플레이하기](https://jaehyun4400.github.io/bps-demo/)**

- 타이틀 → 로비 → 던전 → 전투 플레이 가능
- 편성 / 성장 / 소환 / 픽업 배너 / 이벤트 / 상점 / 우편 / 업적 / 출석 / 리딤코드 포함
- 리딤코드 `POWERPOWER` 입력 시 무제한 자원으로 전 시스템 테스트 가능

---

*© 2026 jaehyun4400 — QA Portfolio Project*
