import pytest

pytestmark = pytest.mark.api

class TestFilmAPI:
    def test_get_all_movies(self, common_user):
        response = common_user.api.movies_api.get_list_all_movies()
        list_response = response.json().get('movies')

        assert isinstance(list_response, list)

    @pytest.mark.slow
    @pytest.mark.parametrize("minPrice,maxPrice,locations,genreID", [
        (150, 350, 'MSK', 1),
        (1, 1000, 'SPB', 10),
        (300, 500, 'MSK', 5)
    ])
    def test_get_movies_with_filters(self, common_user, minPrice, maxPrice, locations, genreID):
        response = common_user.api.movies_api.get_list_all_movies(params={
            'minPrice': minPrice,
            'maxPrice': maxPrice,
            'locations': locations,
            'genreId': genreID
        })
        list_response = response.json().get('movies')
        for e in list_response:
            assert minPrice <= e.get('price') <= maxPrice
            assert e.get('location') == locations
            assert e.get('genreId') == genreID

    def test_create_film(self, super_admin, film_data):
        # Создаем новый фильм
        created_film_response = super_admin.api.movies_api.create_new_film(film_data=film_data)
        response_data = created_film_response.json()

        assert response_data['name'] == film_data['name'], 'Название фильма не совпадает'

    def test_delete_film(self, super_admin, common_user, film_data):
        # Создаем новый фильм
        created_film_response = super_admin.api.movies_api.create_new_film(film_data=film_data)

        # Удаляем этот фильм
        movie_id = created_film_response.json()['id']
        super_admin.api.movies_api.delete_film(movie_id=movie_id)

        # Проверка запроса фильма с этим айдишником
        common_user.api.movies_api.get_one_movie(movie_id, expected_status=404)

    def test_create_review(self, super_admin, review_data, created_film_data):
        movie_id = created_film_data.get('id')
        super_admin.api.movies_api.create_review(movie_id=movie_id, review_data=review_data)

    @pytest.mark.slow
    def test_get_reviews(self, common_user, created_film_data, review_data):
        # Находим айдишник в созданном фильме
        movie_id = created_film_data.get('id')

        # Создаем отзыв с этим айдишником
        common_user.api.movies_api.create_review(movie_id=movie_id, review_data=review_data)

        # Получаем отзывы на фильм с этим айдишником
        reviews_response = common_user.api.movies_api.get_reviews(movie_id=movie_id)
        response_data_dict = reviews_response.json()[0]

        # Проверки
        assert response_data_dict['rating'] == review_data['rating'], 'Рейтинг не совпадает'
        assert response_data_dict['text'] == review_data['text'], 'Текст не совпадает'
        assert 'fullName' in response_data_dict['user'], 'В отзыве нет имени автора'

    @pytest.mark.slow
    def test_create_film_without_authorization(self, common_user, film_data):
        common_user.api.movies_api.create_new_film(film_data=film_data, expected_status=(401, 403))

    def test_delete_film_without_authorization(self, super_admin, common_user, film_data):
        # Создаем новый фильм
        created_film_response = super_admin.api.movies_api.create_new_film(film_data=film_data)

        # Удаляем этот фильм
        movie_id = created_film_response.json()['id']
        common_user.api.movies_api.delete_film(movie_id=movie_id, expected_status=(401, 403))

    @pytest.mark.flaky
    def test_get_nonexistent_movie(self, common_user, non_existent_movie_id):
        response = common_user.api.movies_api.get_one_movie(movie_id=non_existent_movie_id, expected_status=404)

        assert response.json().get('message') == 'Фильм не найден'

    @pytest.mark.slow
    def test_create_review_without_rating(self, common_user, review_data, created_film_data):
        movie_id = created_film_data.get('id')

        invalid_review_data = review_data.copy()
        invalid_review_data['rating'] = None
        common_user.api.movies_api.create_review(movie_id=movie_id, review_data=invalid_review_data, expected_status=400)