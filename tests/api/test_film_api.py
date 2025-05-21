from api.api_manager import ApiManager
from conftest import api_manager
from constants import ADMIN_CREDS

class TestFilmAPI:
    def test_get_all_movies(self, api_manager: ApiManager):
        response = api_manager.movies_api.get_list_all_movies()
        list_response = response.json().get('movies')

        assert isinstance(list_response, list)

    def test_get_movies_with_filters(self, api_manager: ApiManager):
        response = api_manager.movies_api.get_list_all_movies(params={'minPrice': 150, 'maxPrice': 250})
        list_response = response.json().get('movies')
        for e in list_response:
            assert 150 <= e['price'] <= 300

    def test_create_film(self, api_manager: ApiManager, film_data):
        # Логинимся под супер админом
        api_manager.auth_api.authenticate(ADMIN_CREDS)

        # Создаем новый фильм
        created_film_response = api_manager.movies_api.create_new_film(film_data=film_data)
        response_data = created_film_response.json()

        assert response_data['name'] == film_data['name'], 'Название фильма не совпадает'

    def test_delete_film(self, api_manager: ApiManager, film_data):
        # Логинимся под супер админом
        api_manager.auth_api.authenticate(ADMIN_CREDS)

        # Создаем новый фильм
        created_film_response = api_manager.movies_api.create_new_film(film_data=film_data)

        # Удаляем этот фильм
        movie_id = created_film_response.json()['id']
        api_manager.movies_api.delete_film(movie_id=movie_id)

        # Проверка запроса фильма с этим айдишником
        api_manager.movies_api.get_one_movie(movie_id, expected_status=404)

    def test_create_review(self, api_manager: ApiManager, review_data, created_film_data):
        movie_id = created_film_data.get('id')
        api_manager.movies_api.create_review(movie_id=movie_id, review_data=review_data)

    def test_get_reviews(self, api_manager: ApiManager, created_film_data, review_data):
        # Находим айдишник в созданном фильме
        movie_id = created_film_data.get('id')

        # Создаем отзыв с этим айдишником
        api_manager.movies_api.create_review(movie_id=movie_id, review_data=review_data)

        # Получаем отзывы на фильм с этим айдишником
        reviews_response = api_manager.movies_api.get_reviews(movie_id=movie_id)
        response_data_dict = reviews_response.json()[0]

        # Проверки
        assert response_data_dict['rating'] == review_data['rating'], 'Рейтинг не совпадает'
        assert response_data_dict['text'] == review_data['text'], 'Текст не совпадает'
        assert 'fullName' in response_data_dict['user'], 'В отзыве нет имени автора'

    def test_create_film_without_authorization(self, api_manager: ApiManager, film_data):
        api_manager.auth_api.none_authenticate()
        api_manager.movies_api.create_new_film(film_data=film_data, expected_status=401)

    def test_delete_film_without_authorization(self, api_manager: ApiManager, film_data):
        # Логинимся под супер админом
        api_manager.auth_api.authenticate(ADMIN_CREDS)

        # Создаем новый фильм
        created_film_response = api_manager.movies_api.create_new_film(film_data=film_data)

        # Обнуляем аутентифиацию
        api_manager.auth_api.none_authenticate()

        # Удаляем этот фильм
        movie_id = created_film_response.json()['id']
        api_manager.movies_api.delete_film(movie_id=movie_id, expected_status=401)

    def test_get_nonexistent_movie(self, api_manager: ApiManager):
        response_data = api_manager.movies_api.get_list_all_movies().json()
        pageCount = response_data.get('pageCount')
        pageSize = response_data.get('pageSize')
        nonexistent_id = (pageCount * pageSize) + 200

        api_manager.movies_api.get_one_movie(movie_id=nonexistent_id, expected_status=404)

    def test_create_review_without_rating(self, api_manager: ApiManager, review_data, created_film_data):
        movie_id = created_film_data.get('id')

        invalid_review_data = review_data.copy()
        invalid_review_data['rating'] = None
        api_manager.movies_api.create_review(movie_id=movie_id, review_data=invalid_review_data, expected_status=400)