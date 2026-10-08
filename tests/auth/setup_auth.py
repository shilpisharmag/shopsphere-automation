from pathlib import Path
from playwright.sync_api import sync_playwright
from config.settings import (
    BASE_URL,
    STANDARD_PASSWORD,
    STANDARD_USERNAME,)

AUTH_FILE = Path("playwright/.auth/user.json")


def main():

    AUTH_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        page.get_by_placeholder("username").fill(STANDARD_USERNAME)
        page.get_by_placeholder("password").fill(STANDARD_PASSWORD)
        page.get_by_role("button",name = "login").click()
        print("cookies:", context.cookies())
        print(
            "Local storage: ",
            page.evaluate("() =>" \
            "JSON.stringify(localStorage)")

        )

        print(
            "session Storage:",
            page.evaluate("() =>" \
            "JSON.stringify(sessionStorage)")
        )
        print("cookies:", context.cookies())
        page.get_by_text("Products").wait_for()
        
        context.storage_state(path=str(AUTH_FILE))
        browser.close()

if __name__ == "__main__":
    main()
    


        
