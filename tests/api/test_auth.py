from datetime import datetime

import allure
import pytest
from pytest_check import check
from sqlalchemy.orm import Session

from api.api_manager import ApiManager
from constants.roles import Roles
from db_requester.models import UserDBModel
from models.user_model import RegisterUserResponse
from models.user_model import TestUser
from resources.user_creds import SuperAdminCreds

pytestmark = pytest.mark.api

class TestAuthAPI:
    def test_register_user(self, api_manager: ApiManager, test_user):
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)
        register_user_response = RegisterUserResponse(**response.json())

        # Проверки
        assert register_user_response.email == test_user.email, "Email не совпадает"


    def test_register_and_login_user(self, api_manager: ApiManager, registered_user):
        """
        Тест на регистрацию и авторизацию пользователя.
        """
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        # Проверки
        assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"


    def test_login(self, api_manager: ApiManager, auth_user_data): # Обсудить с Николаем фикстуру
        # Создание запроса на аутентификацию
        authorized_response = api_manager.auth_api.login_user(auth_user_data)

        # Проверки
        assert 'accessToken' in authorized_response.json(), 'Token отсутствует в ответе'
        assert authorized_response.json()['user']['email'] == auth_user_data['email'], 'Email ответа не совпадает с отправленным'


    def test_invalid_password(self, api_manager: ApiManager, auth_user_data):
        # Создание неверных данных
        copied_auth_user_data = auth_user_data.copy()
        copied_auth_user_data['password'] = 'incorrect'

        # Создание запроса на аутентификацию с неверным паролем
        bad_password_response = api_manager.auth_api.login_user(copied_auth_user_data, expected_status=401)

        # Проверки
        assert "Неверный логин или пароль" in bad_password_response.text, 'Тело ответа не содержит сообщение об ошибке'


    def test_invalid_email(self, api_manager: ApiManager, auth_user_data):
        # Создание неверных данных
        copied_auth_user_data = auth_user_data.copy()
        copied_auth_user_data['email'] = 'incorrect@gmail.com'

        # Создание запроса на аутентификацию с неверным паролем
        bad_email_response = api_manager.auth_api.login_user(copied_auth_user_data, expected_status=401)

        assert "Неверный логин или пароль" in bad_email_response.text, 'Тело ответа не содержит сообщение об ошибке'


    def test_post_with_empty_body(self, api_manager: ApiManager):
        api_manager.auth_api.login_user(login_data=None, expected_status=401)

    @pytest.mark.parametrize("email,password,expected_status", [
        (f"{SuperAdminCreds.USERNAME}", f"{SuperAdminCreds.PASSWORD}", (200, 201)),
        ("test_login1@email.com", "asdqwe123Q!", (400, 401)),  # Сервис не может обработать логин по незареганному юзеру
        ("", "password", (400, 401)),
    ], ids=["Admin login", "Invalid user", "Empty username"])

    def test_login_with_parametrization(self, email, password, expected_status, api_manager):
        login_data = {
            "email": email,
            "password": password
        }
        api_manager.auth_api.login_user(login_data=login_data, expected_status=expected_status)

    @pytest.mark.db
    def test_register_user_db_session(self, api_manager: ApiManager, test_user: TestUser, db_session: Session):
        """
        Тест на регистрацию пользователя с проверкой в базе данных.
        """
        # выполняем запрос на регистрацию нового пользователя
        response = api_manager.auth_api.register_user(test_user)
        register_user_response = RegisterUserResponse(**response.json())

        # Проверяем добавил ли сервис Auth нового пользователя в базу данных
        users_from_db = db_session.query(UserDBModel).filter(UserDBModel.id == register_user_response.id)

        # получили объект из бзы данных и проверили что он действительно существует в единственном экземпляре
        assert users_from_db.count() == 1, "объект не попал в базу данных"
        # Достаем первый и единственный объект из списка полученных
        user_from_db = users_from_db.first()
        # можем осуществить проверку всех полей в базе данных например Email
        assert user_from_db.email == test_user.email, "Email не совпадает"

    @allure.title("Тест регистрации пользователя с помощью Mock")
    @allure.severity(allure.severity_level.MINOR)
    @allure.label("qa_name", "Ivan Petrovich")
    def test_register_user_mock(self, api_manager: ApiManager, test_user: TestUser, mocker):
        with allure.step(" Мокаем метод register_user в auth_api"):
            mock_response = RegisterUserResponse(  # Фиктивный ответ
                id="id",
                email="email@email.com",
                fullName="fullName",
                verified=True,
                banned=False,
                roles=[Roles.SUPER_ADMIN],
                createdAt=str(datetime.now())
            )

            mocker.patch.object(
                api_manager.auth_api,  # Объект, который нужно замокать
                'register_user',  # Метод, который нужно замокать
                return_value=mock_response  # Фиктивный ответ
            )

        with allure.step("Вызываем метод, который должен быть замокан"):
            register_user_response = api_manager.auth_api.register_user(test_user)

        with allure.step("Проверяем, что ответ соответствует ожидаемому"):
            with allure.step("Проверка поля персональных данных"):  # обратите внимание на вложенность allure.step
                with check:
                    # Строка ниже выдаст исключение, но выполнение теста продолжится
                    #check.equal(register_user_response.fullName, "INCORRECT_NAME", "НЕСОВПАДЕНИЕ fullName")
                    check.equal(register_user_response.email, mock_response.email)

            with allure.step("Проверка поля banned"):
                with check("Проверка поля banned"):  # можно использовать вместо allure.step
                    check.equal(register_user_response.banned, mock_response.banned)