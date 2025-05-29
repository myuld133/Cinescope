import datetime

import pytest
from pytz import timezone

from db_requester.models import MovieDBModel
from utils.data_generator import DataGenerator


class TestOthersAPI:
    @pytest.mark.db
    def test_create_delete_movie(self, api_manager, super_admin, db_session):
        # как бы выглядел SQL запрос
        """SELECT id, "name", price, description, image_url, "location", published, rating, genre_id, created_at
           FROM public.movies
           WHERE name='Test Moviej1h8qss9s5';"""

        movie_name = f"Test Movie{DataGenerator.generate_random_str(10)}"
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)

        # проверяем что до начала тестирования фильма с таким названием нет
        assert movies_from_db.count() == 0, "В базе уже присутствует фильм с таким названием"

        movie_data = { #todo: use model class
            "name": movie_name,
            "price": 500,
            "description": "Описание тестового фильма",
            "location": "MSK",
            "published": True,
            "genreId": 3
        }
        response = super_admin.api.movies_api.create_new_film(film_data=movie_data, expected_status=(200,201))
        response = response.json()

        # проверяем после вызова api_manager.movies_api.create_movie в базе появился наш фильм
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
        assert movies_from_db.count() == 1, "В базе уже присутствует фильм с таким названием"

        movie_from_db = movies_from_db.first()
        # можете обратить внимание, что в базе данных есть поле created_at которое мы не задавали явно
        # наш сервис сам его заполнил. проверим что он заполнил его верно с погрешностью в 5 минут
        assert movie_from_db.created_at >= (
                    datetime.datetime.now(timezone('UTC')).replace(tzinfo=None) - datetime.timedelta(
                minutes=5)), "Сервис выставил время создания с большой погрешностью"

        # Берем айди фильма который мы только что создали и удаляем его из базы через апи
        # Удаляем фильм
        super_admin.api.movies_api.delete_film(movie_id=response["id"])

        # проверяем что в конце тестирования фильма с таким названием действительно нет в базе
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
        assert movies_from_db.count() == 0, "Фильм не был удален из базы!"

    def test_delete_film(self, super_admin, common_user, film_data, db_session, db_test_movie):
        # Создаем новый фильм
        #created_film_response = super_admin.api.movies_api.create_new_film(film_data=film_data)
        db_session.add(db_test_movie)
        db_session.commit()
        # Удаляем этот фильм
        movie_id = db_test_movie.id
        super_admin.api.movies_api.delete_film(movie_id=movie_id)

        # Проверка запроса фильма с этим айдишником
        common_user.api.movies_api.get_one_movie(movie_id, expected_status=404)

        # check movies in db
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.id == movie_id)
        assert movies_from_db.count() == 0, "В базе присутствует фильм с таким id"