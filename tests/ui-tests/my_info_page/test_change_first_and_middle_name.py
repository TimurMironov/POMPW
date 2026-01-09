import allure

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage
from config.data import Data


class TestChangeFirstAndMiddleName:
    TEST_FIRST_NAME = "first name"
    TEST_MIDDLE_NAME = "middle name"

    @allure.title("Логин тест")
    def test_change_first_and_middle_name(self, login_page: LoginPage, dashboard_page: DashboardPage,
                                          my_info_page: MyInfoPage, data: Data):
        login_page.open_page()
        login_page.enter_login(data.LOGIN)
        login_page.enter_password(data.PASSWORD)
        login_page.click_login()
        dashboard_page.is_opened()
        dashboard_page.sidebar.click_my_info_link()
        my_info_page.is_opened()
        my_info_page.set_first_name(self.TEST_FIRST_NAME)
        my_info_page.set_middle_name(self.TEST_MIDDLE_NAME)
        my_info_page.save_personal_details()
        my_info_page.check_first_name_saved(self.TEST_FIRST_NAME)
        my_info_page.check_middle_name_saved(self.TEST_MIDDLE_NAME)
