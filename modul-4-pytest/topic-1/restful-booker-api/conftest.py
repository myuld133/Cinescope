import pytest
import requests
from faker import Faker
from constants import HEADERS, BASE_URL
from custom_requester import CustomRequester

faker = Faker()

@pytest.fixture(scope="session")
def requester():
    """
    Фикстура для создания экземпляра CustomRequester.
    """
    session = requests.Session()
    return CustomRequester(session=session, base_url=BASE_URL)

@pytest.fixture(scope="session")
def requester_with_auth_session(requester):
    requester.session.headers.update(HEADERS)

    response = requester.send_request(method='POST', endpoint='/auth', data={
        "username": "admin",
        "password": "password123"
    })

    token = response.json().get("token")
    assert token is not None, "В ответе не оказалось токена"

    requester.session.headers.update({"Cookie": f"token={token}"})
    return requester


@pytest.fixture
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Cigars"
    }


@pytest.fixture
def put_data():
    return {
      "firstname": "Jane",
      "lastname": "Smith",
      "totalprice": 200,
      "depositpaid": False,
      "bookingdates": {
        "checkin": "2024-12-21",
        "checkout": "2024-12-27"
      },
      "additionalneeds": "Dinner"
    }


@pytest.fixture
def patch_data():
    return {
      "firstname": "Yulka",
      "lastname": "Timof"
    }


@pytest.fixture
def missing_required_data():
    return {
      "firstname": "Jane",
      "lastname": "Smith",
      "depositpaid": False,
      "bookingdates": {
        "checkin": "2024-12-21",
        "checkout": "2024-12-27"
      },
      "additionalneeds": "Dinner"
    }


@pytest.fixture
def invalid_type_data():
    return {
      "firstname": "Jane",
      "lastname": "Smith",
      "totalprice": 'two hundreds',
      "depositpaid": False,
      "bookingdates": {
        "checkin": "2024-12-21",
        "checkout": "2024-12-27"
      },
      "additionalneeds": "Dinner"
    }

@pytest.fixture
def patch_empty_data():
    return {
      "firstname": None,
      "lastname": None
    }

@pytest.fixture
def valid_auth_data():
    return {
        "username": "admin",
        "password": "password123"
    }