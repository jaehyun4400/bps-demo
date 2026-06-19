# CLAUDE.md — BPS 프로젝트 작업 가이드

> Claude Code가 매 세션 시작 시 자동으로 읽는 파일입니다.
> 메모리 유실 방지 목적. 중요 결정사항, 배포 정보, 작업 규칙을 여기에 기록합니다.

---

## 프로젝트 기본 정보

- **프로젝트명**: Blades of Plumflower Beneath Snow (BPS)
- **성격**: 가상의 동양 궁중 판타지 모바일 수집형 방치 RPG — QA 포트폴리오 시각화 데모
- **노션 포트폴리오**: https://www.notion.so/Blades-of-Plumflower-Beneath-Snow-BPS-305ac4dd05a180059009e1779a547e35

---

## 배포 및 저장소

- **GitHub Pages (라이브 데모)**: https://jaehyun4400.github.io/bps-demo/
- **GitHub 저장소**: https://github.com/jaehyun4400/bps-demo (branch: main)
- **배포 명령어**: `git add index.html CLAUDE.md && git commit -m "..." && git push origin main`
- 작업 완료 후 반드시 커밋 + 푸시까지 진행할 것
- index.html 변경 시 CLAUDE.md 구현 현황도 함께 업데이트 후 같이 커밋

---

## 파일 경로

| 구분 | 경로 |
|------|------|
| 메인 작업 파일 | `index.html` (프로젝트 루트) |
| 초상화 이미지 | `portraits_unified/` (gungny.png / choisg.png / gungny2.png / hye.png) |
| SD 치비 캐릭터 | `sd_chars/` (sword_girl.png / bow_girl.png / mage_girl.png / normal_girl.png) |
| 작업 가이드 | `CLAUDE.md` (본 파일) |

> WSL(Claude Code)과 Windows Cursor 환경 파일은 별도로 관리되므로 수동 병합 필요

---

## 협업 규칙

- 작업 완료 시 반드시 **"작업이 완료되었습니다. 지금 확인해보세요!"** 출력
- 커밋 후 **푸시(배포)까지** 자동으로 진행 (별도 요청 없어도)
- 코드 변경 후 항상 `git push origin main` 으로 GitHub Pages 반영
- 중요한 결정사항은 이 파일(CLAUDE.md)과 메모리 파일 양쪽에 기록

---

## CLAUDE.md 관리 결정사항 (2026-04-29)

- 현재 **B 방식**: CLAUDE.md를 git에 커밋하여 GitHub에 공개
- 추후 필요 시 `.gitignore`에 추가하여 A 방식(로컬 전용)으로 전환 가능
- 민감한 정보(토큰, 비밀번호 등)는 절대 이 파일에 기재하지 않음

---

## 게임 구조 핵심 요약

### 캐릭터
| 이름 | 등급 | 패시브 |
|------|------|--------|
| 궁중시녀 | R | 없음 |
| 최상궁 | R | 없음 |
| 궁중의녀 | SR | 전투 시작 시 HP 20% 회복 |
| 혜 귀인 | SSR | HP 60% 이하 시 보호막 발동 (locked, 소환 필요) |

### 무기 설계 원칙

- **모든 캐릭터는 무기 타입 제한 없이 착용 가능** — 캐릭터별 무기 타입 제한 없음
- **orb 타입은 기본 단일 타겟** — 공용 AoE 없음, 범위 공격은 무기 고유 키로만 구현
- **화씨벽 전용 스플래시**: `splashAll:0.15` 키 사용 — 매 공격 주 데미지의 15%를 전체 적에게 추가 피해 (주 타겟 제외)
- **뇌음목 폭발**: `aoeProcChance` + `aoeProcScale` 키 사용 — 확률 발동, 주 타겟 포함 전체 적에게 피해
- 신규 무기에 범위 공격 부여 시 위 키 방식을 따를 것

### 던전 구조
- D1-D4, D6: 10스테이지 (1-(N-1) 일반, N 보스)
- D5, D7: 30스테이지 (`stageCount:30, sections` 구조)
- 필드 모드: 보스 스테이지 제외 전부 (`isFieldMode = !isBossStage`)

### 혜 귀인 보호막 시스템 (2026-04-29 구현 완료)

| 항목 | 내용 |
|------|------|
| 발동 조건 | HP 60% 이하 (일격으로 60% 이하가 되는 경우 포함, 사망 제외) |
| 쉴드량 | 최대 HP의 15% 고정 (HP 증가 시 비례 증가 — 의도된 설계) |
| 데미지 처리 | 쉴드 먼저 차감 → 남은 데미지만 HP 적용 |
| 쿨타임 | 쉴드 소진 시 20초 시작 |
| 재발동 | 쿨타임 종료 시 HP 60% 이하이면 자동 즉시 재발동 |
| 중첩 | 없음 — 재생성 시 항상 15%로 덮어씌움 |
| 스테이지 이동 | 쿨타임 초기화, HP 60% 이하이면 진입 즉시 발동 |
| 적용 대상 | 혜 귀인 전용 패시브 (타 캐릭터는 아이템/의복으로 별도 예정) |

### HP 오브 UI (2026-04-29 교체 완료)

도넛 차트(conic-gradient 56px) → Canvas 기반 디아블로 스타일 액체 구체(72px)

| 요소 | 내용 |
|------|------|
| 렌더링 | Canvas 72×72px, RAF 루프 파도 애니메이션 |
| HP 색상 | 빨강(50%+) / 주황(25%+) / 진빨강(위험) |
| 쉴드 표시 | 오브 내부 HP 위에 하늘색 액체 레이어 |
| 외곽 링 | 활성=파란 펄스 / 쿨타임=회색 dim / 소진=shatter 파열 |
| 보스 모드 | AP HP 바에 파란색 쉴드 구간 추가(`ap-shield-fill`) |

---

## v1.3.0 작업 현황 (2026-06-19)

### 진행 순서
1. ✅ **A. 출석 체크 시스템** — 구현 완료 (2026-06-19)
2. ✅ **B. 혜귀인 픽업 배너** — 구현 완료 (2026-06-19)
3. ✅ **C. 시즌 전환 + 운영 안내 우편** — 구현 완료 (2026-06-19)

> 사용자가 "프리뷰" 라고 입력하면 아래 A 섹션 내용을 출력할 것.

---

### A. 출석 체크 시스템 — 구현 완료 (2026-06-19)

**최종 확정 스펙 (사용자 피드백 반영)**

| 항목 | 내용 |
|---|---|
| 타이틀 | 🌸 여름방학맞이 7days 특별 출석이벤트 |
| 사이클 | 7일 누적 (Day 7 완료 후 Day 1 재시작 — **단, BUG-001(qa/1.3)으로 리셋 미동작**) |
| 출석 방식 | 누적 출석 — 하루 빠져도 이어서 진행 |
| 수령 조건 | 날짜 기준 1일 1회 (`ciTodayStr() !== S.lastCheckIn`) |
| 진입 경로 | ① 게임 접속(로비 진입) 시 자동 팝업(세션 1회) ② 로비 우측 상단 원형 아이콘 클릭 |
| 미수령 표시 | 원형 아이콘 우상단 빨간 뱃지(`#checkin-badge`) |

**보상 설계 (기존 × 500)**

| Day | 보상 | 라벨 |
|---|---|---|
| 1 | 💰 골드 500,000 | 50만 |
| 2 | 💎 다이아 2,500 | 2,500 |
| 3 | 💰 골드 1,500,000 | 150만 |
| 4 | 💎 다이아 5,000 | 5,000 |
| 5 | 💰 골드 2,500,000 | 250만 |
| 6 | 💎 다이아 10,000 | 1만 |
| 7 | 💎 다이아 25,000 (주간 대보상 🎁) | 2.5만 |

**State 구조**
```javascript
checkInDay: 0,       // 완료 일수 = 다음 수령 슬롯 인덱스 (0~7)
lastCheckIn: '',     // 마지막 수령 날짜 'YYYY-MM-DD'  (saveGame/applyData 영속)
// _checkinAutoShown : 세션 1회 자동팝업 플래그 (JS 전역, 비영속)
```
- 수령 가능: `canCheckInToday()` = `ciTodayStr() !== S.lastCheckIn`
- 수령 시: `CHECKIN_REWARDS[checkInDay]` 지급 → lastCheckIn=오늘 → checkInDay++
- 정상 설계: Day 7 수령 후 checkInDay=0 리셋 → 다음 사이클 Day 1 재시작

**의도적 버그 — BUG-001 (Major, `qa/1.3/BUG_REPORT.md` 기준)** ✅ 데모 재현 확인
- `claimCheckIn()` 내 `if(checkInDay>=7) checkInDay=0;` 리셋 라인 주석 처리(누락)
- 결과: Day 7 수령 후 checkInDay=7 고착 → `checkInDay < CHECKIN_REWARDS.length` 조건 false
- → 출석 버튼 **영구 비활성화**, 다음 사이클 진입 불가
- 검증: 브라우저 7일 시뮬레이션 후 8일째 버튼 비활성 확인 (스크린샷 `qa/1.3/attachments/`)

**연결 TC (8개, `qa/1.3/TEST_CASES.md` TC-001~008)**

| 구분 | 시나리오 |
|---|---|
| 경계값 | Day 6 수령 후 Day 7 진입 확인 |
| 경계값 | Day 7 수령 후 Day 1 사이클 리셋 확인 → **FAIL (BUG-001)** |
| 기능 | 당일 수령 후 버튼 비활성화 (중복 방지) |
| 기능 | 자정 이후 날짜 변경 시 수령 버튼 활성화 |
| 기능 | 각 Day별 보상 정확성 확인 (Day 1~7) |
| 기능 | 수령 완료 슬롯 dim+✔ 처리 확인 |
| 기능 | 사이클 리셋 후 Day 1 보상 재지급 확인 → **FAIL (BUG-001)** |
| 회귀 | 출석 수령 후 기존 재화 정상 합산 확인 |

---

### B. 혜귀인 픽업 배너 — 구현 완료 (2026-06-19)

**스펙 (사용자 확정)**

| 항목 | 내용 |
|---|---|
| 형태 | 전용 배너 화면 (`screen-banner`) — 로비 우측 `🌸 픽업소환` 버튼으로 진입 |
| 픽업 대상 | 혜 귀인 (SSR, 신규 캐릭터 없이 기존 캐릭터 활용) |
| 확률 | SSR 1.5% → **3.0%** UP (`pullOne({pickup:true})`), SR 12%, R 나머지 |
| 천장 | **50회 소환 시 혜 귀인 확정** (`GACHA_PITY_CAP=50`, 기존 유지) |
| 소환 옵션 | 1회(💎200) / 10+1(💎1,800, SR 이상 보장) |
| 결과 표시 | 기존 `ov-gacha` 팝업 + `showGachaResult()` 재사용 |

**구성 요소**
- 히어로 배너(혜 귀인 일러스트 + PICK UP), 확률 UP 박스, 천장 게이지(`pk-pity-fill`), 소환 버튼 2종
- `BANNER` 상수: single/multi 소환 설정
- `pullBanner(mode)`: 소환 실행 (pickup 플래그 항상 적용)

**의도적 버그 — BUG-002 (Major, `qa/1.3/BUG_REPORT.md` 기준)** ✅ 데모 재현 확인
- `BANNER.multi.count`가 11이 아닌 **10**으로 설정 → "10+1 소환"인데 10회만 지급
- 증상: 결과 카드 10장, 타이틀도 "소환 결과"(10+1 분기 미적용), 획득 합계 10개
- 검증: 브라우저 10+1 소환 → 카드 10장 확인 (`qa/1.3/attachments/BUG-002_multi_10cards.png`)
- 리포트: `qa/1.3/BUG_REPORT.md` BUG-002 (연결 TC-009)

---

### C. 시즌 전환 + 운영 안내 우편 — 구현 완료 (2026-06-19)

**시즌 전환 (발렌타인 → 여름방학)**
- 타이틀 버전 표기: `v1.2.0 · 두근두근 발렌타인 업데이트` → `v1.3.0 · 신나는 여름방학!! 🌴🏖️`
- `gotoLobby()`에서 발렌타인 이벤트 팝업(`showEvPopup`) 자동 노출 분기 제거 — 로비 진입 시 자동 팝업은 **출석 이벤트 팝업만** 남음
- 발렌타인 이벤트 화면 자체는 유지, 로비 `💕 이벤트` 버튼으로 수동 접근 가능
- 미사용 상태 `S.evShown` 제거

**운영 안내 우편 2종 (`SYSTEM_MAILS` 추가)**
- `mail_update_v130_notice`: 업데이트 안내(여름방학 시즌 + 출석 이벤트 안내, 5줄), 보상 없음, 만료 발송일+30일
- `mail_update_v130_patch`: 점검 완료 안내, 보상 💎3,000+💰1,500,000, 만료 발송일+30일
- 신규/기존 유저 공통 자동 발송 (`injectSystemMails()`는 isNew 무관하게 `SYSTEM_MAILS` 전체 주입)
- 우편 본문 줄바꿈 표시를 위해 `.mail-card-body`에 `white-space:pre-line` 추가

**SAVE_PREFIX 버전 동기화**
- `bps_v120_` → `bps_v130_`로 변경, `SAVE_PREFIX_LEGACY='bps_v120_'`로 하위호환 유지
- `loadSave()`/`getSavedNicks()`는 신규+레거시 prefix 모두 조회, `deleteSave()`는 양쪽 키 모두 삭제
- 기존 데모 플레이 데이터(v1.2.0 시점 저장)가 끊기지 않도록 마이그레이션 안전장치 적용

**코드 주석 버그 번호 동기화**
- `claimCheckIn()`, `BANNER.multi` 주석의 "BUG-003/004" → "BUG-001/002 (qa/1.3 기준)"으로 정정 (qa 폴더 재구성 후 번호가 바뀌었으나 코드 주석은 누락됐던 부분)

**연결 TC**: TC-014(발렌타인 팝업 미노출) · TC-015(타이틀 버전) · TC-016(안내우편) · TC-017(점검보상우편) — `qa/1.3/TEST_CASES.md`

---

## 주요 JS 함수 위치 (index.html)

| 함수 | 역할 |
|------|------|
| `checkShieldPassive()` | 혜 귀인 보호막 발동 조건 체크 (매 틱 호출) |
| `applyShieldAbsorb(dmg)` | 데미지를 쉴드로 먼저 차감 |
| `drawHpOrb()` | Canvas HP 오브 렌더링 (RAF 루프) |
| `startOrbAnim()` / `stopOrbAnim()` | HP 오브 애니메이션 시작/중지 |
| `advanceBattleStage()` | 스테이지 진행, 쉴드/쿨타임 리셋 + 즉시 발동 체크 |
| `initFieldUI()` | 필드 모드 초기화 + 오브 생성 |
| `renderPlayer()` | 플레이어 HP/쉴드 UI 갱신 |
| `doAttackAnim(onHit,targetIdx)` | 무기 타입별 공격 발사체 + 이펙트 처리 |
| `showRingImpact(x,y,bColor,fColor)` | 링 충격파 공용 함수 (bow=파랑 / orb=빨강 / 미착용=황금) |
| `showPunchImpact(x,y)` | `showRingImpact` 황금색 래퍼 (미착용 전용) |
| `openCheckIn()` | 출석 팝업 열기 (`renderCheckIn` 호출 후 ov-checkin active) |
| `renderCheckIn()` | 7일 그리드 + 수령 버튼 상태 렌더 |
| `claimCheckIn()` | 오늘 출석 보상 수령 (⚠ BUG-001[1.3] 리셋 누락 지점) |
| `canCheckInToday()` / `ciTodayStr()` | 오늘 수령 가능 여부 / 'YYYY-MM-DD' 반환 |
| `updateCheckInBadge()` | 원형 아이콘 미수령 뱃지 표시/숨김 |
| `openBanner()` / `renderBanner()` | 픽업 배너 진입 / 천장·재화·일러스트 렌더 |
| `pullBanner(mode)` | 픽업 소환 실행 (mode 1=1회, 10=10+1, ⚠ BUG-002[1.3] 지점) |
| `pullOne(opts)` | 단일 소환 추첨 (opts.pickup 시 SSR 3%, 천장 50) |
