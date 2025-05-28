import json
import logging
import os

from pydantic import BaseModel

from constants.constants import RED, GREEN, RESET


class CustomRequester:
    base_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


    def __init__(self, session, base_url):
        """
        Инициализация кастомного реквестера.
        :param session: Объект requests.Session.
        :param base_url: Базовый URL API.
        """
        self.base_url = base_url
        self.headers = self.base_headers.copy()
        self.session = session
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)


    def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True, params=None):
        """
        Универсальный метод для отправки запросов.
        :param method: HTTP метод (GET, POST, PUT, DELETE и т.д.).
        :param endpoint: Эндпоинт (например, "/login").
        :param data: Тело запроса (JSON-данные).
        :param expected_status: Ожидаемый статус-код (по умолчанию 200).
        :param need_logging: Флаг для логирования (по умолчанию True).
        :param params: Query-параметры.
        :return: Объект ответа requests.Response.
        """
        url = f"{self.base_url}{endpoint}"

        if isinstance(data, BaseModel):
            data = json.loads(data.model_dump_json(exclude_unset=True))

        response = self.session.request(method, url, json=data, headers=self.headers, params=params)
        if need_logging:
            self.__log_request_and_response(response)

        if isinstance(expected_status, int):
            if response.status_code != expected_status:
                raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status}")
        if isinstance(expected_status, tuple):
            if response.status_code not in expected_status:
                raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status}")

        return response

    def __log_request_and_response(self, response):
        """
        Логгирование запросов и ответов. Настройки логгирования описаны в pytest.ini
        Преобразует вывод в curl-like (-H хэдэеры), (-d тело)

        :param response: Объект response получаемый из метода "send_request"
        """
        try:
            request = response.request
            headers = " \\\n".join([f"-H '{header}: {value}'" for header, value in request.headers.items()])
            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"

            body = ""
            if hasattr(request, 'body') and request.body is not None:
                if isinstance(request.body, bytes):
                    body = request.body.decode('utf-8')
                elif isinstance(request.body, str):
                    body = request.body
                body = f"-d '{body}' \n" if body != '{}' else ''

            self.logger.info(
                f"{GREEN}{full_test_name}{RESET}\n"
                f"curl -X {request.method} '{request.url}' \\\n"
                f"{headers} \\\n"
                f"{body}"
            )

            response_status = response.status_code
            is_success = response.ok
            response_data = response.text
            if not is_success:
                self.logger.info(f"\tRESPONSE:"
                                 f"\nSTATUS_CODE: {RED}{response_status}{RESET}"
                                 f"\nDATA: {RED}{response_data}{RESET}")
        except Exception as e:
            self.logger.info(f"\nLogging went wrong: {type(e)} - {e}")

    def _update_session_headers(self, **kwargs):
        """
        Обновление заголовков сессии.
        :param kwargs: Дополнительные заголовки.
        """
        self.headers.update(kwargs)  # Обновляем базовые заголовки
        self.session.headers.update(self.headers)  # Обновляем заголовки в текущей сессии
