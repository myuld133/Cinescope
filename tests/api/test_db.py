import datetime

import pytest
from pytz import timezone

from conftest import film_data

pytest.mark = pytest.mark.db
class TestDB:
    def test_create_movie(self, super_admin, film_data, db_helper):
        # проверяем что до начала тестирования фильма с таким названием нет
        assert not db_helper.movie_exists_by_name(film_data['name']), 'Фильм с таким названием уже существует'

        # создаем фильм через манагера
        response_data = super_admin.api.movies_api.create_new_film(film_data=film_data).json()

        # проверяем после вызова api_manager.movies_api.create_movie в базе появился наш фильм
        assert db_helper.movie_exists_by_name(response_data['name']), "В базе уже присутствует фильм с таким названием"

        # можете обратить внимание, что в базе данных есть поле created_at которое мы не задавали явно
        # наш сервис сам его заполнил. проверим что он заполнил его верно с погрешностью в 5 минут
        assert db_helper.get_movie_by_id(response_data['id']).created_at >= (
                    datetime.datetime.now(timezone('UTC')).replace(tzinfo=None) - datetime.timedelta(
                minutes=5)), "Сервис выставил время создания с большой погрешностью"

    def test_delete_movie(self, super_admin, db_test_movie, db_helper):
        # Создаем новый фильм
        db_helper.create_movie(db_test_movie.to_dict())

        # Удаляем этот фильм
        movie_id = db_test_movie.id
        super_admin.api.movies_api.delete_film(movie_id=movie_id)

        # Проверка запроса фильма с этим айдишником после удаления
        assert not db_helper.movie_exists_by_id(db_test_movie.id), "В базе присутствует фильм с таким id"


    def test_db_requests(self, super_admin, db_helper, created_test_user):
        assert created_test_user == db_helper.get_user_by_id(created_test_user.id)
        assert db_helper.user_exists_by_email("api1@gmail.com")
