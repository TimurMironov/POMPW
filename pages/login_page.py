import allure
from playwright.sync_api import expect, Page

from config.links import Links
from pages.base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_URL

    USERNAME_LOCATOR = "//input[@name='username']"
    PASSWORD_LOCATOR = "//input[@name='password']"
    LOGIN_BUTTON_LOCATOR = "//button[@type='submit']"

    def __init__(self, page:Page) -> None:
        super().__init__(page)
        self.username_locator = page.locator(self.USERNAME_LOCATOR)
        self.password_locator = page.locator(self.PASSWORD_LOCATOR)
        self.login_button = page.locator(self.LOGIN_BUTTON_LOCATOR)

    def enter_login(self, login):
        with allure.step(f"Ввести логин - {login}"):
            expect(self.username_locator, "Поле ввода логина не пустое").to_be_empty()
            self.username_locator.fill(login)

    def enter_password(self, password):
        with allure.step(f"Ввести пароль - {password}"):
            expect(self.password_locator, "Поле ввода пароля не пустое").to_be_empty()
            self.password_locator.fill(password)

    def click_login(self):
        with allure.step("Нажать кнопку войти"):
            self.login_button.click()
