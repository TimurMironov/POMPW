import allure
from playwright.sync_api import Page


class SideBarComponent:
    MY_INFO_BUTTON_LOCATOR = "//span[text()='My Info']"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.my_info_button_locator = self.page.locator(self.MY_INFO_BUTTON_LOCATOR)

    def click_my_info_link(self):
        with allure.step("Кликнуть на ссылку 'My info'"):
            self.my_info_button_locator.click()
