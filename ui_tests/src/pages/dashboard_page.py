from playwright.sync_api import Page

from ui_tests.src.config.links import Links
from ui_tests.src.pages.base_page import BasePage


class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_URL

    def __init__(self, page: Page):
        super().__init__(page)

