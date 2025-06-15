import time

import pytest

from ui_objects.cinescope_pages import CinescopLoginPage
from utils.tools import Tools

DEFAULT_UI_TIMEOUT = 30000

@pytest.fixture(scope='session')
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope='function')
def context(browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    context.set_default_timeout(DEFAULT_UI_TIMEOUT)
    yield context
    log_name = f"trace_{Tools.get_timestamp()}.zip"
    trace_path = Tools.files_dir('playwright_trace', log_name)
    context.tracing.stop(path=trace_path)
    context.close()

@pytest.fixture(scope='function')
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope='function')
def loginpage(page, common_user):
    login_page = CinescopLoginPage(page)
    login_page.open()
    login_page.login(common_user.email, common_user.password)
    time.sleep(5)
    return page