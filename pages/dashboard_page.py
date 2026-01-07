import allure
from playwright.sync_api import Page

from config.links import Links
from pages.base_page import BasePage


class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_URL

    MY_INFO_BUTTON_LOCATOR = "//span[text()='My Info']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.my_info_button_locator = self.page.locator(self.MY_INFO_BUTTON_LOCATOR)

    def click_my_info_link(self):
        with allure.step("Кликнуть на ссылку 'My info'"):
            self.my_info_button_locator.click()

