import time
import pytest

from playwright.sync_api import Page, expect
from datetime import date


def test_text_box(page: Page):
    page.goto('https://demoqa.com/text-box')

    # вариант №3
    page.fill(selector='#userName', value='testQa')
    page.fill(selector='#userEmail', value='testemail@gmail.com')
    page.fill(selector='#currentAddress', value='20, Lenina st, SPB')
    page.fill(selector='#permanentAddress', value='18, Baker st, London')

    page.click('#submit')  # а можно сразу селектор передать внутрь метода click()

    time.sleep(8)

    expect(page.locator('#output #name')).to_have_text('Name:testQa')
    expect(page.locator('#output #email')).to_have_text('Email:testemail@gmail.com')
    expect(page.locator('#output #currentAddress')).to_have_text('Current Address :20, Lenina st, SPB')
    expect(page.locator('#output #permanentAddress')).to_have_text('Permananet Address :18, Baker st, London')


def test_web_tables(page: Page):
    page.goto('https://demoqa.com/webtables')
    #1
    page.get_by_role('button', name='Add').click()
    #2
    expect(page.get_by_text("Registration Form")).to_be_visible()
    time.sleep(5)
    #3
    page.get_by_placeholder("First Name").fill('Ann')
    page.get_by_placeholder("Last Name").fill('Stark')
    page.get_by_placeholder("name@example.com").fill('adm34874@mail.ru')
    page.get_by_placeholder("Age").fill('25')
    page.get_by_placeholder("Salary").type('300000') # посимвольный ввод
    page.get_by_placeholder("Department").fill('IT')
    time.sleep(5)
    page.get_by_role('button', name='Submit').click()

    time.sleep(5)

def test_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')

    #2 проверка значения по умолчанию
    today_date = date.today().strftime("%d %b %Y")
    assert page.get_attribute('#dateOfBirthInput', 'value') == today_date  # bug

    #1 заполнение формы
    page.get_by_role("textbox", name="First Name").fill('Piter')
    page.get_by_role("textbox", name="Last Name").fill('Parker')
    page.get_by_role("textbox", name="name@example.com").type('adms23847@mail.com')
    page.locator('label[for="gender-radio-1"]').click()
    page.get_by_role("textbox", name="Mobile Number").type('9274653387')
    page.locator("#dateOfBirthInput").click()
    page.select_option('.react-datepicker__year-select', '2000')
    page.select_option('.react-datepicker__month-select', 'May')
    page.get_by_role("option", name="Choose Thursday, May 18th,").click()
    page.locator('label[for="hobbies-checkbox-1"]').click()
    page.locator('label[for="hobbies-checkbox-2"]').click()
    page.get_by_role("textbox", name="Current Address").fill('20, Baker str, London')
    page.locator("#state").click()
    page.get_by_text('NCR', exact=True).click() # кастомная реализация выпадающего списка
    page.locator("#city").click()
    page.get_by_text('Noida', exact=True).click()

    time.sleep(5)

    #3 проверка содержания футера
    assert page.locator('footer span').text_content() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_radio_button(page: Page):
    page.goto('https://demoqa.com/radio-button')

    # проверка активности 2 радиобаттонов и неактивности 3-го
    assert page.get_by_role('radio', name='Yes').is_enabled(), "Радиокнопка Yes не активна"
    assert page.get_by_role('radio', name='Impressive').is_enabled(), "Радиокнопка Impressive не активна"
    assert not page.get_by_role('radio', name='No').is_enabled(), "Радиокнопка No активна"

def test_checkbox(page: Page):
    page.goto('https://demoqa.com/checkbox')

    #1 проверка, что Home виден, а Desktop не виден
    assert page.get_by_text('Home', exact=True).is_visible(), "Home не виден"
    assert not page.get_by_text('Desktop', exact=True).is_visible(), "Desktop виден"

    #2
    page.get_by_role("button", name="Toggle").click()

    #3
    assert page.get_by_text('Desktop', exact=True).is_visible(), "Desktop виден"

@pytest.mark.flaky(reruns=3)
def test_dynamic_properties(page: Page):
    page.goto('https://demoqa.com/dynamic-properties') # страница прогружается долго
    #1
    assert not page.get_by_role("button", name="Visible After 5 Seconds").is_visible(timeout=1000), 'Кнопка есть'
    #2
    page.wait_for_selector('#visibleAfter')

def test_radio_button_with_expects(page: Page):
    page.goto('https://demoqa.com/radio-button')

    expect(page.get_by_role('radio', name='Yes')).to_be_enabled()
    expect(page.get_by_role('radio', name='Impressive')).to_be_enabled()
    expect(page.get_by_role('radio', name='No')).to_be_disabled()

    page.locator('[for="yesRadio"]').click()

    expect(page.get_by_role('radio', name='Yes')).to_be_checked()
    expect(page.get_by_role('radio', name='Impressive')).not_to_be_checked()
    expect(page.get_by_role('radio', name='No')).not_to_be_checked()