import allure
from playwright.sync_api import Page, expect

from pages.components import SideBarComponent


class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def open_page(self):
        with allure.step(f"Открыть страницу {self.PAGE_URL}"):
            self.page.context.clear_cookies()
            self.page.goto(self.PAGE_URL, timeout=60000)
            self.page.wait_for_load_state("networkidle")

    def is_opened(self):
        with allure.step(f"Проверить, что открыта страница {self.PAGE_URL}"):
            self.page.wait_for_load_state("networkidle")
            expect(self.page).to_have_url(self.PAGE_URL, timeout=60000)

    def make_screenshot(self):
        allure.attach(
            body=self.page.screenshot(),
            name="screenshot.png",
            attachment_type=allure.attachment_type.PNG
        )

    @property
    def sidebar(self):
        return SideBarComponent(self.page)