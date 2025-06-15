import allure
import pytest

from ui_objects.cinescope_pages import CinescopeReviewPage


@allure.epic("Тестирование UI")
@allure.feature("Тестирование отзывов")
@pytest.mark.ui
class TestloginPage:
    @allure.title("Создание корректного отзыва")
    def test_review_by_ui(self, loginpage, common_user):
        review_page = CinescopeReviewPage(loginpage)
        review_page.open_movie()

        review_page.create_new_review('Очень хорошее кино!', '5')
        review_page.make_screenshot_and_attach_to_allure()
        review_page.assert_allert_was_pop_up()

        #time.sleep(3)