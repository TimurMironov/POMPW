import pytest
from playwright.sync_api import BrowserContext, Browser
from config.data import Data


@pytest.fixture(scope="session")
def auth_cookies(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    data = Data()

    page.goto("https://opensource-demo.orangehrmlive.com/", timeout=60000)
    page.fill("input[name='username']", data.LOGIN)
    page.fill("input[name='password']", data.PASSWORD)
    page.click("button[type='submit']")
    page.wait_for_url("**/dashboard/**", timeout=150000)

    cookies = context.cookies()
    context.close()

    return cookies


@pytest.fixture(scope='function')
def auth_via_cookie(context: BrowserContext, auth_cookies):
    context.add_cookies(auth_cookies)
    return context