from playwright.sync_api import sync_playwright
import time
import pytest

@pytest.mark.skip(reason='сайт не загружается')
def test_first_browser():
    # Создаем экземпляр Playwright и запускаем его
    playwright = sync_playwright().start()

    # Далее, используя объект playwright, можно запускать браузер и работать с ним
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://demoqa.com/')
    time.sleep(10)  # Сделаем sleep иначе браузер сразу закроется перейдя к следующим строкам

    # После выполнения необходимых действий, следует явно закрыть браузер
    browser.close()

    # И остановить Playwright, чтобы освободить ресурсы
    playwright.stop()

def test_multiple_browsers():
    with sync_playwright() as p:
        chromium_browser = p.chromium.launch(headless=False)
        firefox_browser = p.firefox.launch(headless=False)

        chromium_page = chromium_browser.new_page()
        firefox_page = firefox_browser.new_page()

        chromium_page.goto("https://www.example.com")
        firefox_page.goto("https://www.google.com")

        time.sleep(10)

        chromium_browser.close()
        firefox_browser.close()

def test_multiple_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page1 = context.new_page()  # Первая страница (вкладка)
        page2 = context.new_page()  # Вторая страница (вкладка)

        # ... (работаем с page1 и page2)

        context.close()
        browser.close()

def test_some_entities():
    with sync_playwright() as p:
        # Запускаем браузер
        browser1 = p.chromium.launch(headless=False)

        # создаем 2 контекста
        context1_1 = browser1.new_context()
        context1_2 = browser1.new_context()

        # В каждом контексте создаем по 2 пейджи
        page1_1_1 = context1_1.new_page()
        page1_1_2 = context1_1.new_page()
        page1_2_1 = context1_2.new_page()
        page1_2_2 = context1_2.new_page()

        # переходим на разные сайты
        page1_1_1.goto("https://www.example.com")
        page1_1_2.goto("https://www.google.com")
        page1_2_1.goto("https://www.wikipedia.org")
        page1_2_2.goto("https://www.yandex.ru")

        # немного ждем, чтобы осмотреться
        time.sleep(10)

        # Закрываем пейджи
        page1_1_1.close()
        page1_1_2.close()
        page1_2_1.close()
        page1_2_2.close()

        # Закрываем контексты
        context1_1.close()
        context1_2.close()

        # Закрываем браузер
        browser1.close()


#использование фикстур в тестах
def test_example(page):  # page автоматически будет предоставлена фикстурой
    page.goto("https://www.example.com")
    time.sleep(10)

def test_google(page):  # page автоматически будет предоставлена фикстурой
    page.goto("https://www.google.com")
    time.sleep(10)


#использование таймаутов в тестах
def test_search_product(page):
    page.goto('https://www.example.com')  # Глобальный таймаут (из фикстуры context)

    page.fill('input#search', 'Playwright', timeout=5000)  # Локальный таймаут для заполнения поля

    page.click('button#search-button')  # Глобальный таймаут

    page.wait_for_selector('.results', state='visible', timeout=10000)  # Локальный таймаут для ожидания результатов поиска

    assert page.locator('.results').count() > 0

# @pytest.mark.timeout(120000)  # Устанавливаем таймаут для всего теста 2 минуты
# def test_long_process(page):
# # ... код теста, выполняющийся длительное время
