import allure
import pytest

from ui_objects.cinescope_pages import CinescopRegisterPage


@allure.epic("Тестирование UI")
@allure.feature("Тестирование Страницы Register")
@pytest.mark.ui
class TestRegisterPage:
    @allure.title("Проведение успешной регистрации")
    def test_register_by_ui(self, test_user, page):
            register_page = CinescopRegisterPage(page)

            register_page.open()
            register_page.register(f"PlaywrightTest {test_user.fullName}", test_user.email, test_user.password,
                                   test_user.passwordRepeat)

            register_page.assert_was_redirect_to_login_page()
            register_page.make_screenshot_and_attach_to_allure()
            register_page.assert_allert_was_pop_up()

            #time.sleep(5)