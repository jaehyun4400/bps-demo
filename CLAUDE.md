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
- **배포 명령어**: `git add index.html && git commit -m "..." && git push origin main`
- 작업 완료 후 반드시 커밋 + 푸시까지 진행할 것

---

## 파일 경로

| 구분 | 경로 |
|------|------|
| 메인 작업 파일 (WSL) | `/home/jhpark/claude/study/bps/index.html` |
| Windows Cursor 파일 | `c:\Users\jh_pa\Cursor\test\index.html` |
| 초상화 이미지 | `portraits_unified/` (gungny.png / choisg.png / gungny2.png / hye.png) |
| SD 치비 캐릭터 | `sd_chars/` (sword_girl.png / bow_girl.png / mage_girl.png / normal_girl.png) |

> WSL과 Windows Cursor 파일은 별도 세션에서 작업되므로 수동 병합 필요

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

### 던전 구조
- D1~D4, D6: 10스테이지 (1~(N-1) 일반, N 보스)
- D5, D7: 30스테이지 (`stageCount:30, sections` 구조)
- 필드 모드: 보스 스테이지 제외 전부 (`isFieldMode = !isBossStage`)

### 혜 귀인 보호막 시스템 (2026-04-29 구현)
- HP 60% 이하 시 최대 HP의 15% 보호막 자동 발동
- 소진 후 쿨타임 20초, 쿨타임 종료 시 HP 여전히 60% 이하이면 즉시 재발동
- 쿨타임은 스테이지 클리어 시 초기화
- 쉴드 수치는 최대 HP의 15% 고정 (중첩 없음)
- HP 오브: Canvas 기반 디아블로 스타일 액체 구체 (도넛 차트 → 교체됨)

### HP 오브 UI
- Canvas 72×72px, RAF 루프로 파도치는 액체 애니메이션
- 빨강(HP 50%+) / 주황(25%+) / 진빨강(위험)
- 쉴드 시 오브 내부에 하늘색 액체 레이어 추가 표시
- 외곽 링: 쉴드 활성=파란 펄스, 쿨타임=회색, 소진=파열(shatter) 애니메이션

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
