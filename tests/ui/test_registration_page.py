import time
from random import randint

from playwright.sync_api import Page, expect


def test_registration(page: Page):
    page.goto('https://dev-cinescope.coconutqa.ru/register')

    # вариант №1
    username_locator = '[data-qa-id="register_full_name_input"]'
    email_locator = '[data-qa-id="register_email_input"]'
    password_locator = '[data-qa-id="register_password_input"]'
    repeat_password_locator = '[data-qa-id="register_password_repeat_input"]'

    user_email = f'test{randint(1, 9999)}@mail.ru'

    page.fill(username_locator, 'Тестов Тестер Тестерович')
    page.fill(email_locator, user_email)
    page.fill(password_locator, 'qwerty123Q')
    page.fill(repeat_password_locator, 'qwerty123Q')

    time.sleep(5)
    page.click('[data-qa-id="register_submit_button"]')

    page.wait_for_url('https://dev-cinescope.coconutqa.ru/login', timeout=60000)
    expect(page.get_by_text("Подтвердите свою почту")).to_be_visible(visible=True)
    time.sleep(5)