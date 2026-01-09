from playwright.sync_api import Page

from config.links import Links
from pages.base_page import BasePage


class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_URL

    def __init__(self, page: Page):
        super().__init__(page)

