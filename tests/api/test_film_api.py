from api.api_manager import ApiManager
from conftest import api_manager
from constants import ADMIN_CREDS

class TestFilmAPI:
    def test_get_all_movies(self, api_manager: ApiManager):
        response = api_manager.movies_api.get_list_all_movies()

        assert isinstance(response, list)

    def test_get_movies_with_filters(self, api_manager: ApiManager):
        response = api_manager.movies_api.get_list_all_movies(params={'minPrice': 150, 'maxPrice': 250})

        for e in response:
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
        deleted_film_response = api_manager.movies_api.delete_film(movie_id=movie_id)

        # Проверка запроса фильма с этим айдишником
        api_manager.movies_api.get_one_movie(movie_id, expected_status=404)

    def test_get_reviews(self, api_manager: ApiManager, film_data, review_data):
        # Логинимся под супер админом
        api_manager.auth_api.authenticate(ADMIN_CREDS)

        # Создаем фильм
        created_movie_response = api_manager.movies_api.create_new_film(film_data=film_data)
        movie_id = created_movie_response.json()['id']

        # Создаем отзыв
        created_review_response = api_manager.movies_api.create_review(movie_id=movie_id, review_data=review_data, expected_status=201)

        # Получаем отзывы на фильм с этим айдишником
        reviews_response = api_manager.movies_api.get_reviews(movie_id=movie_id)
        response_data_dict = reviews_response.json()[0]

        # Проверки
        assert response_data_dict['rating'] == review_data['rating'], 'Рейтинг не совпадает'
        assert response_data_dict['text'] == review_data['text'], 'Текст не совпадает'
        assert 'fullName' in response_data_dict['user'], 'В отзыве нет имени автора'