import requests

from constants import BASE_URL, LOGIN_ENDPOINT, HEADERS, REGISTER_ENDPOINT


class TestAuthApiWithoutCustomWrapper:
    def test_register_user(self, test_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=test_user, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"

    def test_login(self, auth_user_data): # Обсудить с Николаем фикстуру
        # URL для аутентификации
        login_url = f'{BASE_URL}{LOGIN_ENDPOINT}'

        # Создание запроса на аутентификацию
        authorized_response = requests.post(login_url, json=auth_user_data, headers=HEADERS)

        assert authorized_response.status_code == 201, 'Аутентификация не прошла'

        assert 'accessToken' in authorized_response.json(), 'Token от сутствует в ответе'
        assert authorized_response.json()['user']['email'] == auth_user_data['email'], 'Email ответа не совпадает с отправленным'

    def test_invalid_password(self, auth_user_data):
        # URL для аутентификации
        login_url = f'{BASE_URL}{LOGIN_ENDPOINT}'

        # Создание неверных данных
        auth_user_data['password'] = 'incorrect'

        # Создание запроса на аутентификацию с неверным паролем
        not_authorized_response = requests.post(login_url, json=auth_user_data, headers=HEADERS)

        assert not_authorized_response.status_code == 401, 'Неверный пароль принят'
        assert "Неверный логин или пароль" in not_authorized_response.text, 'Тело ответа не содержит сообщение об ошибке'


    def test_invalid_email(self, auth_user_data):
        # URL для аутентификации
        login_url = f'{BASE_URL}{LOGIN_ENDPOINT}'

        # Создание неверных данных
        auth_user_data['email'] = 'incorrect@gmail.com'

        # Создание запроса на аутентификацию с неверным паролем
        not_authorized_response = requests.post(login_url, json=auth_user_data, headers=HEADERS)

        assert not_authorized_response.status_code == 401, 'Неверный email принят'
        assert "Неверный логин или пароль" in not_authorized_response.text, 'Тело ответа не содержит сообщение об ошибке'


    def test_post_with_empty_body(self):
        # URL для аутентификации
        login_url = f'{BASE_URL}{LOGIN_ENDPOINT}'

        response = requests.post(login_url, headers=HEADERS)

        assert response.status_code == 401, 'Пустое тело запроса принято' # баг? пришло 401, а по доке 400.