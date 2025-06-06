import datetime

import allure
import pytest
import sqlalchemy
from pytz import timezone
from sqlalchemy.orm import Session

from db_requester.models import AccountTransactionTemplate
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

    def test_delete_film(self, super_admin, common_user, film_data, db_session, db_test_movie, db_connection):
        # Создаем новый фильм
        #created_film_response = super_admin.api.movies_api.create_new_film(film_data=film_data)
        stmt = sqlalchemy.insert(MovieDBModel.__table__).values(
            id = db_test_movie.id,
            name = db_test_movie.name,
            description = db_test_movie.description,
            price = db_test_movie.price,
            genre_id = db_test_movie.genre_id,
            image_url = db_test_movie.image_url,
            location = db_test_movie.location,
            rating = db_test_movie.rating,
            published = db_test_movie.published,
            created_at = db_test_movie.created_at
        )
        db_connection.execute(stmt)
        db_connection.commit()

        # Удаляем этот фильм
        movie_id = db_test_movie.id
        super_admin.api.movies_api.delete_film(movie_id=movie_id)

        # Проверка запроса фильма с этим айдишником
        common_user.api.movies_api.get_one_movie(movie_id, expected_status=404)

        # check movies in db
        movies_from_db = db_session.query(MovieDBModel).filter(MovieDBModel.id == movie_id)
        assert movies_from_db.count() == 0, "В базе присутствует фильм с таким id"


@allure.epic("Тестирование транзакций")
@allure.feature("Тестирование транзакций между счетами")
class TestAccountTransactionTemplate:

    @allure.story("Корректность перевода денег между двумя счетами")
    @allure.description("""
    Этот тест проверяет корректность перевода денег между двумя счетами.
    Шаги:
    1. Создание двух счетов: Stan и Bob.
    2. Перевод 200 единиц от Stan к Bob.
    3. Проверка изменения балансов.
    4. Очистка тестовых данных.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("qa_name", "Ivan Petrovich")
    @allure.title("Тест перевода денег между счетами 200 рублей")
    def test_accounts_transaction_template(self, db_session: Session):
        # ====================================================================== Подготовка к тесту
        with allure.step("Создание тестовых данных в базе данных: счета Stan и Bob"):
            stan = AccountTransactionTemplate(user=f"Stan_{DataGenerator.generate_random_int(10)}", balance=1000)
            bob = AccountTransactionTemplate(user=f"Bob_{DataGenerator.generate_random_int(10)}", balance=500)
            db_session.add_all([stan, bob])
            db_session.commit()

        @allure.step("Функция перевода денег: transfer_money")
        @allure.description("""
            функция выполняющая транзакцию, имитация вызова функции на стороне тестируемого сервиса
            и вызывая метод transfer_money, мы какбудтобы делем запрос в api_manager.movies_api.transfer_money
            """)
        def transfer_money(session, from_account, to_account, amount):
            with allure.step(" Получаем счета"):
                from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
                to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()

            with allure.step("Проверяем, что на счете достаточно средств"):
                if from_account.balance < amount:
                    raise ValueError("Недостаточно средств на счете")

            with allure.step("Выполняем перевод"):
                from_account.balance -= amount
                to_account.balance += amount

            with allure.step("Сохраняем изменения"):
                session.commit()

        # ====================================================================== Тест
        with allure.step("Проверяем начальные балансы"):
            assert stan.balance == 1000
            assert bob.balance == 500

        try:
            with allure.step("Выполняем перевод 200 единиц от stan к bob"):
                transfer_money(db_session, from_account=stan.user, to_account=bob.user, amount=200)

            with allure.step("Проверяем, что балансы изменились"):
                assert stan.balance == 800
                assert bob.balance == 700

        except Exception as e:
            with allure.step("ОШИБКА откаты транзакции"):
                db_session.rollback()

            pytest.fail(f"Ошибка при переводе денег: {e}")

        finally:
            with allure.step("Удаляем данные для тестирования из базы"):
                db_session.delete(stan)
                db_session.delete(bob)
                db_session.commit()