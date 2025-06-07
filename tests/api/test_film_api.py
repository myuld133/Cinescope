import allure
import pytest

from models.movie_model import CreatedMovieResponse


@allure.epic('Cinescope')
@allure.feature('Тестирование Movies Api')
@pytest.mark.api
class TestFilmAPI:
    @allure.story('Получение фильмов')
    @allure.title('Получение списка всех фильмов')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_movies(self, common_user):
        with allure.step("Отправка запроса для получения списка всех фильмов"):
            response = common_user.api.movies_api.get_list_all_movies()
        with allure.step("Проверка, что ответ содержит список фильмов"):
            list_response = response.json().get('movies')
            assert isinstance(list_response, list), 'Ответ должен содержать несколько фильмов'

    @allure.story("Получение фильмов")
    @allure.title("Получение фильмов с заданными фильтрами")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.slow
    @pytest.mark.parametrize("minPrice,maxPrice,locations,genreID", [
        (150, 350, 'MSK', 1),
        (1, 1000, 'SPB', 10),
        (300, 500, 'MSK', 5)
    ])
    def test_get_movies_with_filters(self, common_user, minPrice, maxPrice, locations, genreID):
        with allure.step(
                f"Запрос фильмов с параметрами: minPrice={minPrice}, "
                f"maxPrice={maxPrice}, "
                f"locations={locations}, "
                f"genreID={genreID}"):
            response = common_user.api.movies_api.get_list_all_movies(params={
                'minPrice': minPrice,
                'maxPrice': maxPrice,
                'locations': locations,
                'genreId': genreID
            })
        with allure.step("Проверка корректности фильтрации"):
            list_response = response.json().get('movies')
            for movie in list_response:
                assert minPrice <= movie.get('price') <= maxPrice, f"Цена фильма {movie.get('price')} вне диапазона {minPrice}-{maxPrice}"
                assert movie.get('location') == locations, f"Локация фильма {movie.get('location')} не соответствует {locations}"
                assert movie.get('genreId') == genreID, f"Жанр фильма {movie.get('genreId')} не соответствует {genreID}"

    @allure.story("Создание фильмов")
    @allure.title("Создание фильма с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_film(self, super_admin, film_data):
        with allure.step("Создание нового фильма через API"):
            response = super_admin.api.movies_api.create_new_film(film_data)
            created_film = CreatedMovieResponse(**response.json())

        with allure.step("Проверка корректности созданного фильма"):
            assert created_film.name == film_data['name'], 'Название фильма не совпадает'
            assert created_film.id is not None, 'ID фильма не был присвоен'

    @allure.story("Удаление фильмов")
    @allure.title("Удаление фильма с ролью Super_Admin")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_film(self, super_admin, common_user, film_data):
        with allure.step("Создание нового тестового фильма через API"):
            response = super_admin.api.movies_api.create_new_film(film_data=film_data)
            created_film = CreatedMovieResponse(**response.json())

        with allure.step("Удаление существующего фильма через API"):
            super_admin.api.movies_api.delete_film(movie_id=created_film.id)

        with allure.step("Проверка, что фильм с таким id отсутствует"):
            common_user.api.movies_api.get_one_movie(created_film.id, expected_status=404)

    @allure.story("Создание отзывов")
    @allure.title("Создание отзыва с ролью User")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_review(self, common_user, review_data, created_film):
        with allure.step("Создание отзыва на существующий фильм"):
            created_review = common_user.api.movies_api.create_review(movie_id=created_film.id, review_data=review_data)
            created_review_data = created_review.json()

        with allure.step("Проверка корректности созданного отзыва"):
            assert created_review_data['rating'] == review_data['rating']
            assert created_review_data['text'] == review_data['text']

    @allure.story("Получение отзывов")
    @allure.title("Получение отзыва на фильм по его id")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.slow
    def test_get_reviews(self, common_user, created_film, review_data):
        with allure.step("Создание отзыва на существующий фильм"):
            common_user.api.movies_api.create_review(movie_id=created_film.id, review_data=review_data)

        with allure.step("Получение этого отзыва на фильм по его id"):
            reviews_response = common_user.api.movies_api.get_reviews(movie_id=created_film.id)
            response_data_dict = reviews_response.json()[0]

        with allure.step("Проверка корректности полученного отзыва"):
            assert response_data_dict['rating'] == review_data['rating'], 'Рейтинг не совпадает'
            assert response_data_dict['text'] == review_data['text'], 'Текст не совпадает'
            assert 'fullName' in response_data_dict['user'], 'В отзыве нет имени автора'

    @allure.story("Создание фильма")
    @allure.title("Создание фильма с ролью User (недостаточно прав)")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("negative")
    @pytest.mark.slow
    def test_create_film_without_authorization(self, common_user, film_data):
        with allure.step("Создание фильма с ролью User и проверка ошибки в ответе"):
            common_user.api.movies_api.create_new_film(film_data=film_data, expected_status=(401, 403))

    @allure.story("Удаление фильма")
    @allure.title("Удаление фильма с ролью User (недостаточно прав)")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("negative")
    def test_delete_film_without_authorization(self, super_admin, common_user, film_data):
        with allure.step("Создание тестового фильма"):
            created_film_response = super_admin.api.movies_api.create_new_film(film_data=film_data)

        with allure.step("Удаление существующего фильма с ролью User"):
            movie_id = created_film_response.json()['id']
            deleted_film_response = common_user.api.movies_api.delete_film(movie_id=movie_id, expected_status=(401, 403))

        with allure.step("Проверка ошибки в ответе"):
            assert deleted_film_response.json().get('error') == "Forbidden"

    @allure.story("Получение фильмов")
    @allure.title("Получение фильма по несуществующему id")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("negative")
    @pytest.mark.flaky
    def test_get_nonexistent_movie(self, common_user, non_existent_movie_id):
        with allure.step("Получение фильма по несуществующему id через API"):
            response = common_user.api.movies_api.get_one_movie(movie_id=non_existent_movie_id, expected_status=404)

        with allure.step("Проверка корректности сообщения об ошибке"):
            assert response.json().get('message') == 'Фильм не найден'

    @allure.story("Создание отзывов")
    @allure.title("Создание отзыва без обязательного поля rating")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("negative")
    @pytest.mark.slow
    def test_create_review_without_rating(self, common_user, review_data, created_film):
        with allure.step("Подготовка данных для отзыва с rating = None"):
            invalid_review_data = review_data.copy()
            invalid_review_data['rating'] = None

        with allure.step("Создание отзыва с невалидными данными и проверка статуса ответа"):
            common_user.api.movies_api.create_review(
                movie_id=created_film.id,
                review_data=invalid_review_data,
                expected_status=400)