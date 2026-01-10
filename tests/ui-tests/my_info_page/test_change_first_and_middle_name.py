import allure

from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


class TestChangeFirstAndMiddleName:
    TEST_FIRST_NAME = "first name"
    TEST_MIDDLE_NAME = "middle name"

    @allure.title("Проверка сохранения изменений полей first name и middle name")
    def test_change_first_and_middle_name(self, my_info_page: MyInfoPage, auth_via_cookie):
        my_info_page.open_page()
        my_info_page.is_opened()
        my_info_page.set_first_name(self.TEST_FIRST_NAME)
        my_info_page.set_middle_name(self.TEST_MIDDLE_NAME)
        my_info_page.save_personal_details()
        my_info_page.check_first_name_saved(self.TEST_FIRST_NAME)
        my_info_page.check_middle_name_saved(self.TEST_MIDDLE_NAME)
