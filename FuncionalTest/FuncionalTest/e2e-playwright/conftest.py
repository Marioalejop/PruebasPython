import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Solo cuando falla el test
    if result.when == "call" and result.failed:
        page = item.funcargs.get("page")

        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")