import pytest


DEFAULT_UI_TIMEOUT = 30000

@pytest.fixture(scope='session')
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope='function')
def context(browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    context.set_default_timeout(DEFAULT_UI_TIMEOUT)
    yield context
    context.close()

@pytest.fixture(scope='function')
def page(context):
    page = context.new_page()
    yield page
    page.close()