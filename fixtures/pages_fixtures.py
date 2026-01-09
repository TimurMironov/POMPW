import pytest
from playwright.sync_api import Page

from config.data import Data
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage


@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture(scope="function")
def dashboard_page(page: Page):
    return DashboardPage(page)

@pytest.fixture(scope="function")
def my_info_page(page: Page):
    return MyInfoPage(page)

@pytest.fixture(scope="class")
def data():
    return Data()