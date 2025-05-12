import requests

# сделать гет-запрос
# response1 = requests.get('https://restful-booker.herokuapp.com/booking')
#
# data = response1.json()

# print(f'Статус ответа: {response.status_code}')
# #print(f'Тело ответа: {response.text}')
# # print(f'Тело ответа: {data}')

# booking_id = 62
# response2 = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
#
# data2 = response2.json()
#
# print(f'Тело ответа: {data2}')

# # передать параметр
# response3 = requests.get('https://restful-booker.herokuapp.com/booking',
#                         params={'firstname': 'Sally'})
#
# data3 = response3.json()
#
# # Тело ответа в словаре
# print(f"Тело ответа: {data3}")


# Создаём словарь с заголовками
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
#     'Accept': 'application/json'
# }
#
# # Передаём заголовки в запрос
# response4 = requests.get(
#     'https://restful-booker.herokuapp.com/booking',
#     headers=headers
# )


# обработка ошибок
# try:
# # Делаем запрос
#     booking_id = 62
#     response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
#
# # Проверяем статус ответа
#     response.raise_for_status()  # Вызовет исключение, если статус не 2XX
#
# # Если всё хорошо, работаем с данными
#     data = response.json()
#     print(f"Получены данные: {data}")

# except requests.exceptions.ConnectionError:
#     print("Не удалось подключиться к серверу")
# # Тут можно, например, повторить запрос позже
#
# except requests.exceptions.Timeout:
#     print("Сервер не отвечает слишком долго")
# # Тут можно увеличить время ожидания и повторить
#
# except requests.exceptions.HTTPError as http_err:
#     print(f"Произошла HTTP ошибка: {http_err}")
# # Например, можно проверить статус код и принять решение что делать
#
# except requests.exceptions.RequestException as e:
#     print(f"Произошла ошибка при выполнении запроса: {e}")
# # Это общий класс ошибок requests


# # post-запросы
#
# # делаем словарь для отправки
# data = {
#     "firstname": "Jim",
#     "lastname": "Brown",
#     "totalprice": 111,
#     "depositpaid": True,
#     "bookingdates": {
#         "checkin": "2025-01-04",
#         "checkout": "2025-01-15"
#     },
#     "additionalneeds": "Breakfast"
# }
#
# # отправляем наш запрос
# response = requests.post(
#     'https://restful-booker.herokuapp.com/booking', json=data)
#
# print(response.json())


# # задание 1
# def test_booking_post():
#     url = 'https://restful-booker.herokuapp.com/booking'
#     data5 = {
#             "firstname": "Yulka",
#             "lastname": "Timoff",
#             "totalprice": 213,
#             "depositpaid": True,
#             "bookingdates": {
#                 "checkin": "2025-05-05",
#                  "checkout": "2025-05-15"
#             },
#             "additionalneeds": "Breakfast"
#     }
#     response5 = requests.post(url, json=data5)
#     assert response5.status_code == 200
#
# # задание 2
#     response_data = response5.json()
#     booking_id = response_data['bookingid']
#
#     response6 = requests.get(f'{url}/{booking_id}')
#     print(response6.json())


# # отправка пейлоада
# url = 'https://restful-booker.herokuapp.com/booking'
# payload = {
#     "firstname": "Jim",
#     "lastname": "Brown",
#     "totalprice": 111,
#     "depositpaid": True,
#     "bookingdates": {
#         "checkin": "2025-01-04",
#         "checkout": "2025-01-15"
#     },
#     "additionalneeds": "Breakfast"
# }

# response = requests.post(url=url, json=payload)
# print(response.text)
# print(response.request.body)
# print(response.request.headers)

# response = requests.post(url=url, data=payload)
# print(response.text)
# print(response.request.body)
# print(response.request.headers)

# # отправили xml
# url = "https://httpbin.org/post"
# data = "<xml><data>some data</data></xml>"  # Отправка XML
# response = requests.post(url, data=data, headers={'Content-Type': 'application/xml'})
#
# print(response.request.headers)
# print(response.request.body)
# print('\n', response.text)

# # отправляем простой текст
# data_bytes = "raw bytes dataЮ"
# response_bytes = requests.post(url, data=data_bytes, headers={'Content-Type': 'text/plain'})
# print(response_bytes.request.headers)
# print(response_bytes.request.body)
# print('\n', response_bytes.encoding)


# # что есть в response
# import requests
#
# url = "https://httpbin.org/get"
# response = requests.get(url)
#
# print(f"Status Code: {response.status_code}")
# print(f"Headers: {response.headers}")
# print(f"Content (bytes): {response.content}")
# print(f"Text (string): {response.text}")
# print(f"JSON: {response.json()}")
# print(f"URL: {response.url}")
# print(f"History: {response.history}")
# print(f"Cookies: {response.cookies}")
# print(f"Encoding: {response.encoding}")
# print(f"Elapsed Time: {response.elapsed}")
# print(f"Request: {response.request}")
# print(f"Reason: {response.reason}")


# # декодирование json
# import requests
#
# urls = [
#     "https://httpbin.org/json",  # Нормальный JSON
#     "https://httpbin.org/status/204", # Пустой ответ
#     "https://httpbin.org/status/500",  # Ошибка 500
#     "https://httpbin.org/html", # HTML
# ]
#
# for url in urls:
#     print(f"URL: {url}")
#     response = requests.get(url)
#     print(f"Status code: {response.status_code}")
#     try:
#         data = response.json()
#         print(f"JSON data: {data}")
#     except requests.exceptions.JSONDecodeError:
#         print(f"Ошибка декодирования JSON. Текст ответа: {response.text}") # Выводим первые 100 символов
#     except Exception as e:
#         print(f"Другая ошибка: {e}")
#     print("-" * 20)


## обработка xml и html
# from bs4 import BeautifulSoup # Для HTML
# import lxml.etree as ET # Для XML
#
# url_html = "https://httpbin.org/html"
# response_html = requests.get(url_html)
# soup = BeautifulSoup(response_html.text, 'html.parser')
# print(soup.title)
#
# url_xml = "https://www.w3schools.com/xml/note.xml"
# response_xml = requests.get(url_xml)
# tree = ET.fromstring(response_xml.content)
# print(tree.find('to').text)


# # сессионные куки
# s = requests.Session()
#
# # Указываем cookie для первого запроса
# response = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print(response.text)
#
# # второй запрос не использует cookie
# response = s.get('https://httpbin.org/cookies')
# print(response.text)


# # сравнить время с сессией и без
# import requests
# import time
#
# url = "https://httpbin.org/get"
# num_requests = 5
#
# print("Запросы с использованием сессии:")
# start_time = time.time()
#
# session = requests.Session()  # Создаем сессию
# try:
#     for i in range(num_requests):
#         response = session.get(url)
#         response.raise_for_status()
# except Exception as e:
#     print(f"ошибка: {e}")
# finally:
#     session.close()  # закрываем сессию
# end_time = time.time()
# print(f"Время выполнения с сессией: {end_time - start_time:.4f} секунд\n")
#
# # Запросы БЕЗ использования сессии:
# print("Запросы БЕЗ использования сессии:")
# start_time = time.time()
# try:
#     for i in range(num_requests):
#         response = requests.get(url)
#         response.raise_for_status()
# except Exception as e:
#     print(f"Ошибка: {e}")
# end_time = time.time()
# print(f"Время выполнения без сессии: {end_time - start_time:.4f} секунд")


# # basic authentication
# import requests
# from requests.auth import HTTPBasicAuth
#
# url = "https://httpbin.org/basic-auth/user/passwd"  # URL, требующий Basic Auth
#
# response = requests.get(url, auth=HTTPBasicAuth('user', 'passwd'))
#
# print(f"Status code: {response.status_code}")
# print(response.json())


# # bearer token
# import requests
#
# url = "https://httpbin.org/bearer"
# token = "my_secret_token"
# headers = {'Authorization': f'Bearer {token}'}
#
# response = requests.get(url, headers=headers)
#
# print(f"Status code: {response.status_code}")
# print(response.json())


# # api key в заголовках
# import requests
#
# url = "https://httpbin.org/headers"
# api_key = "my_api_key"
# headers = {'X-API-Key': api_key}
#
# response = requests.get(url, headers=headers)
#
# print(f"Status code: {response.status_code}")
# print(response.json()) # В json будет информация о переданных заголовках, включая X-API-Key


# # api key в параметрах
# import requests
#
# url = "https://httpbin.org/get"
# api_key = "my_api_key"
# params = {'api_key': api_key}
#
# response = requests.get(url, params=params)
#
# print(f"Status code: {response.status_code}")
# print(response.json()) # В json будет информация о переданных параметрах, включая api_key

## refresh token
# import requests
#
# REFRESH_TOKEN_URL = "https://example.com/api/token/refresh"
#
# refresh_token = "YOUR_REFRESH_TOKEN"
#
# def refresh_access_token(refresh_token):
#     """Обновляет access токен с помощью refresh токена."""
#     data = {"refresh_token": refresh_token}
#     response = requests.post(REFRESH_TOKEN_URL, json=data)
#
#     if response.status_code == 200:
#         new_access_token = response.json().get("access_token")
#         new_refresh_token = response.json().get("refresh_token")
#         return new_access_token, new_refresh_token
#     else:
#         print(f"Ошибка обновления токена: {response.status_code}")
#         return None, None
#
# # Получаем оба токена
# new_access_token, new_refresh_token = refresh_access_token(refresh_token)
#
# if new_access_token: # проверка что не None
#     print(f"Новый access токен: {new_access_token}")
#     if new_refresh_token:
#         print(f"Новый refresh токен: {new_refresh_token}")
#
#     # Дальше суем в заголовок/куки - в зависимости от реализации
#     headers = {"Authorization": f"Bearer {new_access_token}"}
#     response = requests.get("https://example.com/api/protected", headers=headers)
#     # ...