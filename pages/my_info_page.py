from pathlib import Path

import allure
from playwright.sync_api import Page, expect

from config.links import Links
from pages.base_page import BasePage


class MyInfoPage(BasePage):
    PAGE_URL = Links.MYINFO_URL

    FIRST_NAME_LOCATOR = "//input[@name='firstName']"
    MIDDLE_NAME_LOCATOR = "//input[@name='middleName']"
    SAVE_BUTTON_LOCATOR = "//button[@type='submit']"
    LOADING_SPINNER_LOCATOR = "//div[@class='oxd-loading-spinner']"
    ADD_ATTACHMENT_BUTTON_LOCATOR = "//button[text()=' Add ']"

    INPUT_ATTACHMENT_LOCATOR = "//input[@type='file']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_locator = page.locator(self.FIRST_NAME_LOCATOR)
        self.middle_name_locator = page.locator(self.MIDDLE_NAME_LOCATOR)
        self.save_personal_details_locator = page.locator(self.SAVE_BUTTON_LOCATOR).nth(0)
        self.loading_spinner_locator = page.locator(self.LOADING_SPINNER_LOCATOR)
        self.add_attachment_locator = page.locator(self.ADD_ATTACHMENT_BUTTON_LOCATOR)
        self.save_attachments = page.locator(self.SAVE_BUTTON_LOCATOR).nth(2)

    def set_first_name(self, first_name):
        with allure.step(f"В поле 'first_name' ввести имя {first_name}"):
            self.first_name_locator.wait_for(state="visible")
            self.first_name_locator.clear()
            expect(self.first_name_locator).to_be_empty()
            self.first_name_locator.fill(first_name)

    def set_middle_name(self, middle_name):
        with allure.step(f"В поле 'middle_name' ввести имя {middle_name}"):
            self.first_name_locator.wait_for(state="visible")
            self.middle_name_locator.clear()
            expect(self.middle_name_locator).to_be_empty()
            self.middle_name_locator.fill(middle_name)

    def save_personal_details(self):
        with allure.step("Сохранить изменения персональных данных"):
            self.save_personal_details_locator.click()
            self.loading_spinner_locator.wait_for(state="detached")

    def check_first_name_saved(self, check_first_name):
        with allure.step(f"Проверка что в поле first_name значение изменилось на {check_first_name}"):
            expect(self.first_name_locator).to_have_value(check_first_name)

    def check_middle_name_saved(self, check_middle_name):
        with allure.step(f"Проверка что в поле middle_name значение изменилось на {check_middle_name}"):
            expect(self.middle_name_locator).to_have_value(check_middle_name)

    def add_attachment(self, path_file):
        self.add_attachment_locator.click()
        self.page.set_input_files(self.INPUT_ATTACHMENT_LOCATOR, path_file)
        self.attachment_name = Path(path_file).name

    def save_attachments_click(self):
        self.save_attachments.click()

    def check_save_attachments(self, test_image=None):
        if hasattr(self, "attachment_name") and test_image is None:
            test_image = self.attachment_name
        attachment_name = self.page.locator(f"//div[text() = '{test_image}']")
        expect(attachment_name).to_be_visible()




