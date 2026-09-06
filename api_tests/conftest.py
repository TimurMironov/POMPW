import pytest


# До всего
def pytest_sessionstart(session):
    print("\n=== API TEST SESSION START ===")


# После всего
def pytest_sessionfinish(session, exitstatus):
    print("\n=== API TEST SESSION FINISH ===")


# До setup fixtures
def pytest_runtest_setup(item):
    print(f"\n=== SETUP: {item.name} ===")


# Перед тестом
def pytest_runtest_call(item):
    print(f"\n=== CALL: {item.name} ===")


# Перед teardown
def pytest_runtest_teardown(item, nextitem):
    print(f"\n=== TEARDOWN: {item.name} ===")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    print(f"REPORT: {item.name} | phase={report.when} | outcome={report.outcome}")
