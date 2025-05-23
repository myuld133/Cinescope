import pytest

from api.api_manager import ApiManager
from resources.user_creds import SuperAdminCreds

pytestmark = pytest.mark.api

class TestAuthAPI:
    def test_register_user(self, api_manager: ApiManager, test_user):
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


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