import random

import pytest
import requests
from faker import Faker

from api.api_manager import ApiManager
from constants import ADMIN_CREDS
from utils.data_generator import DataGenerator

faker = Faker('ru_RU')

@pytest.fixture(scope='function')
def test_user():
    """
    Генерация случайного пользователя для тестов
    """
    random_email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_password = DataGenerator.generate_random_password()

    return {
        'email': random_email,
        'fullName': random_name,
        'password': random_password,
        'passwordRepeat': random_password,
        'roles': ['USER']
    }


@pytest.fixture(scope='function')
def auth_user_data(api_manager, test_user):
    # Регистрируем нового пользователя
    api_manager.auth_api.register_user(test_user)
    # Создаем словарь с входными данными
    auth_data = {'email': test_user['email'],
                 'password': test_user['password']
                 }
    return auth_data


@pytest.fixture(scope="function")
def registered_user(api_manager, test_user):
    """
    Фикстура для регистрации и получения данных зарегистрированного пользователя.
    """
    response = api_manager.auth_api.register_user(test_user)

    response_data = response.json()
    registered_user = test_user.copy()
    registered_user["id"] = response_data["id"]
    return registered_user


@pytest.fixture(scope="session")
def session():
    """
    Фикстура для создания HTTP-сессии.
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(session):
    """
    Фикстура для создания экземпляра ApiManager.
    """
    return ApiManager(session)


@pytest.fixture(scope='function')
def film_data():
    """
    Генерация случайного фильма для тестов
    """
    locations = ['SPB', 'MSK']

    return {
        "name": faker.catch_phrase(),
        "imageUrl": faker.url(),
        "price": faker.random_int(min=100, max=1000),
        "description": faker.text(),
        "location": random.choice(locations),
        "published": faker.boolean(),
        "genreId": faker.random_int(min=1, max=10)
    }

@pytest.fixture()
def review_data():
    return {
        'rating': random.randint(1, 5),
        'text': faker.sentence()
    }

@pytest.fixture()
def created_film_data(api_manager: ApiManager, film_data):
    api_manager.auth_api.authenticate(ADMIN_CREDS)

    # Создаем новый фильм
    created_film_response = api_manager.movies_api.create_new_film(film_data=film_data)
    created_film_data = created_film_response.json()

    yield created_film_data

    # Удаляем фильм
    movie_id = created_film_data.get('id')
    api_manager.movies_api.delete_film(movie_id=movie_id)