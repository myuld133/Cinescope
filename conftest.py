import random

import pytest
import requests
from faker import Faker

from api.api_manager import ApiManager
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
    random_name = faker.catch_phrase()
    random_url = faker.url()
    random_price = faker.random_int()
    random_description = faker.text()
    locations = ['SPB', 'MSK']
    random_location = random.choice(locations)
    random_published = faker.boolean()
    random_genreId = faker.random_int(min=1, max=3)

    return {
        "name": random_name,
        "imageUrl": random_url,
        "price": random_price,
        "description": random_description,
        "location": random_location,
        "published": random_published,
        "genreId": random_genreId
    }

@pytest.fixture()
def review_data():
    random_rating = random.randint(1, 5)
    random_text = faker.sentence()

    return {
        'rating': random_rating,
        'text': random_text
    }