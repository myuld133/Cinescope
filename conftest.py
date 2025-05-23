import random

import pytest
import requests
from faker import Faker

from api.api_manager import ApiManager
from constants.roles import Roles
from entities.user import User
from resources.user_creds import SuperAdminCreds
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
        'roles': [Roles.USER.value]
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
def created_film_data(super_admin, film_data):
    # Создаем новый фильм
    created_film_response = super_admin.api.movies_api.create_new_film(film_data=film_data)
    created_film_data = created_film_response.json()

    yield created_film_data

    # Удаляем фильм
    movie_id = created_film_data.get('id')
    super_admin.api.movies_api.delete_film(movie_id=movie_id)

@pytest.fixture()
def non_existent_movie_id(common_user):
    response_data = common_user.api.movies_api.get_list_all_movies().json()

    pageCount = response_data.get('pageCount')
    pageSize = response_data.get('pageSize')
    nonexistent_id = (pageCount * pageSize) + 2000000

    return nonexistent_id

@pytest.fixture
def user_session():
    user_pool = []

    def _create_user_session():
        session = requests.Session()
        user_session = ApiManager(session)
        user_pool.append(user_session)
        return user_session

    yield _create_user_session

    for user in user_pool:
        user.close_session()

@pytest.fixture
def super_admin(user_session):
    new_session = user_session()

    super_admin = User(
        SuperAdminCreds.USERNAME,
        SuperAdminCreds.PASSWORD,
        list(Roles.SUPER_ADMIN.value),
        new_session
    )

    super_admin.api.auth_api.authenticate(super_admin.creds)
    return super_admin

@pytest.fixture(scope='function')
def creation_user_data(test_user):
    updated_data = test_user.copy()
    updated_data.update({
        'verified': True,
        'banned': False
    })
    return updated_data

@pytest.fixture
def common_user(user_session, super_admin, creation_user_data):
    new_session = user_session()

    common_user = User(
        creation_user_data['email'],
        creation_user_data['password'],
        list(Roles.USER.value),
        new_session
    )

    super_admin.api.user_api.create_user(creation_user_data)
    common_user.api.auth_api.authenticate(common_user.creds)
    return common_user

@pytest.fixture
def admin(user_session, super_admin, creation_user_data):
    new_session = user_session()

    admin = User(
        creation_user_data['email'],
        creation_user_data['password'],
        list(Roles.ADMIN.value),
        new_session
    )

    super_admin.api.user_api.create_user(creation_user_data)
    admin.api.auth_api.authenticate(admin.creds)
    return admin