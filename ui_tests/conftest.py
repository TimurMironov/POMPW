import allure
import pytest

from ui_tests.src.fixtures import *

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.outcome == "failed":
        if 'page' in item.fixturenames:
            page = item.funcargs['page']
            allure.attach(
                page.screenshot(),
                name="screenshot.png",
                attachment_type=allure.attachment_type.PNG
            )
