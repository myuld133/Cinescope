from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT


class TestAuthAPI:
    def test_register_user(self, requester, test_user):
        """
        Тест на регистрацию пользователя.
        """
        response = requester.send_request(
            method="POST",
            endpoint=REGISTER_ENDPOINT,
            data=test_user,
            expected_status=201
        )
        response_data = response.json()

        # Проверки
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    def test_register_and_login_user(self, requester, registered_user):
        """
        Тест на регистрацию и авторизацию пользователя.
        """
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = requester.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=login_data,
            expected_status=201
        )
        response_data = response.json()

        # Проверки
        assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"


    def test_login(self, requester, auth_user_data): # Обсудить с Николаем фикстуру
        # Создание запроса на аутентификацию
        authorized_response = requester.send_request(
            method='POST',
            endpoint=LOGIN_ENDPOINT,
            data=auth_user_data,
            expected_status=201
        )

        # Проверки
        assert 'accessToken' in authorized_response.json(), 'Token отсутствует в ответе'
        assert authorized_response.json()['user']['email'] == auth_user_data['email'], 'Email ответа не совпадает с отправленным'


    def test_invalid_password(self, requester, auth_user_data):
        # Создание неверных данных
        auth_user_data['password'] = 'incorrect'

        # Создание запроса на аутентификацию с неверным паролем
        not_authorized_response = requester.send_request(
            method='POST',
            endpoint=LOGIN_ENDPOINT,
            data=auth_user_data,
            expected_status=401
        )

        # Проверки
        assert "Неверный логин или пароль" in not_authorized_response.text, 'Тело ответа не содержит сообщение об ошибке'


    def test_invalid_email(self, requester, auth_user_data):
        # Создание неверных данных
        auth_user_data['email'] = 'incorrect@gmail.com'

        # Создание запроса на аутентификацию с неверным паролем
        not_authorized_response = requester.send_request(
            method='POST',
            endpoint=LOGIN_ENDPOINT,
            data=auth_user_data,
            expected_status=401
        )

        assert "Неверный логин или пароль" in not_authorized_response.text, 'Тело ответа не содержит сообщение об ошибке'


    def test_post_with_empty_body(self, requester):
        # Отправка запроса с пустым телом
        requester.send_request(
            method='POST',
            endpoint=LOGIN_ENDPOINT,
            data=None,
            expected_status=401
        )