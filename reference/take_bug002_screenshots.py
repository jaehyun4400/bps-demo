"""
BUG-002 재현 스크린샷 촬영 스크립트
대례복 착용 후 전투력(cp-disp) UI 미갱신 버그

1. BUG-002_before.png  — 의복 탭, 대례복 미착용, cp-disp 정상값
2. BUG-002_during.png  — 대례복 착용 직후, cp-disp 여전히 이전값 (버그)
3. BUG-002_after.png   — 로비 재진입 후 편성 재진입, cp-disp 갱신됨
"""
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML_PATH = Path(__file__).resolve().parent.parent / "index.html"
OUT_DIR   = Path(__file__).resolve().parent / "attachments"
OUT_DIR.mkdir(exist_ok=True)

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 420, "height": 760})
        page.goto(f"file://{HTML_PATH}")
        page.wait_for_load_state("networkidle")
        time.sleep(0.5)

        # ── 로그인 화면: 닉네임 입력 후 게임 시작
        page.fill("#login-nick", "QA테스터")
        page.click("text=게임 시작 ▶")
        time.sleep(0.5)

        # ── 타이틀 화면 클릭 → 로비로
        page.click("#screen-title")
        time.sleep(0.6)

        # 이벤트 팝업이 뜨면 닫기 (500ms 후에 뜨므로 1초 대기)
        time.sleep(1.0)
        try:
            ov = page.locator("#ov-event")
            if ov.is_visible():
                page.evaluate("closeOv('ov-event')")
                time.sleep(0.3)
        except Exception:
            pass

        # ── 편성 화면으로 이동 (하단 네비 "편성" 버튼)
        page.click("button:has-text('편성')", timeout=5000)
        time.sleep(0.5)

        # ── 의복 탭 클릭
        page.click("button.ltab:has-text('의복')", timeout=3000)
        time.sleep(0.4)

        # CP 값 확인 (Before)
        cp_before = page.locator("#cp-disp").text_content()
        print(f"[Before] cp-disp = {cp_before}")
        page.screenshot(path=str(OUT_DIR / "BUG-002_1_before_equip.png"))
        print("✅ BUG-002_1_before_equip.png 저장")

        # ── 대례복 착용 클릭
        daerye_card = page.locator(".equip-card").filter(has_text="대례복").first
        daerye_card.click()
        time.sleep(0.5)

        # CP 값 확인 (During — 버그: 갱신 안 됨)
        cp_during = page.locator("#cp-disp").text_content()
        print(f"[During] cp-disp = {cp_during}")
        page.screenshot(path=str(OUT_DIR / "BUG-002_2_after_equip.png"))
        print("✅ BUG-002_2_after_equip.png 저장")

        # ── 로비 재진입 → 편성 재진입 (After: 정상 복구)
        page.evaluate("goScreen('lobby')")
        time.sleep(0.4)
        page.evaluate("goScreen('lineup')")
        time.sleep(0.4)
        page.click("button.ltab:has-text('의복')", timeout=3000)
        time.sleep(0.4)

        cp_after = page.locator("#cp-disp").text_content()
        print(f"[After]  cp-disp = {cp_after}")
        page.screenshot(path=str(OUT_DIR / "BUG-002_3_reentry.png"))
        print("✅ BUG-002_3_reentry.png 저장")

        # ── 결과 검증
        print()
        if cp_before == cp_during and cp_during != cp_after:
            print("🎯 BUG-002 재현 성공!")
            print(f"  착용 전 : {cp_before}")
            print(f"  착용 후  : {cp_during}  ← 갱신 안 됨 (버그)")
            print(f"  재진입 후: {cp_after}  ← 갱신됨 (정상)")
        else:
            print("⚠️  버그 재현 결과 확인 필요")
            print(f"  before={cp_before}, during={cp_during}, after={cp_after}")

        browser.close()

if __name__ == "__main__":
    run()
