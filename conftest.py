import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,slow_mo=2000,
            args=["--start-maximized"]
        )

        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        yield page

        #  Proper teardown (IMPORTANT)
        page.set_default_timeout(5000)
        context.close()
        browser.close()