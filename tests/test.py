import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage
from config.data import Data


class TestLoginPage:

    TEST_FIRST_NAME = "first name"
    TEST_MIDDLE_NAME = "middle name"

    @pytest.fixture(autouse=True)
    def setup_method(self, page: Page):
        self.data = Data()
        self.login_page = LoginPage(page)
        self.dashboard_page = DashboardPage(page)
        self.my_info_page = MyInfoPage(page)

    @allure.title("Логин тест")
    def test_login(self):
        self.login_page.open_page()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.my_info_page.is_opened()
        self.my_info_page.set_first_name(self.TEST_FIRST_NAME)
        self.my_info_page.set_middle_name(self.TEST_MIDDLE_NAME)
        self.my_info_page.save_personal_details()
        self.my_info_page.check_first_name_saved(self.TEST_FIRST_NAME)
        self.my_info_page.check_middle_name_saved(self.TEST_MIDDLE_NAME)
        self.my_info_page.make_screenshot()