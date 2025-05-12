import pytest
import requests
from faker import Faker
from constants import BASE_URL

class TestBookings:
    fake = Faker()

    def test_create_booking(self, auth_session, booking_data):
        # Создаём бронирование
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"

        # Проверяем, что бронирование можно получить по ID
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"


    def test_update_booking(self, auth_session, booking_data, put_data):
        # Создаем бронирование и проверяем, что оно создалось
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        # Обновляем данные бронирования
        booking_id = create_booking.json()['bookingid']
        put_booking_response = auth_session.put(f'{BASE_URL}/booking/{booking_id}', json=put_data)
        assert put_booking_response.status_code == 200, 'Данные не обновились'

        # Проверяем, что данные действительно обновились
        updated_booking = auth_session.get(f'{BASE_URL}/booking/{booking_id}')
        assert updated_booking.status_code == 200, 'Не удалось получить данные обновленного бронирования'
        assert updated_booking.json() == put_data, 'Измененные данные не совпадают'


    def test_patch_booking(self, auth_session, booking_data, patch_data):
        # Создаем бронирование и проверяем, что оно создалось
        created_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert created_booking.status_code == 200, "Ошибка при создании брони"

        #  Частично обновляем данные бронирования - имя и фамилию
        booking_id = created_booking.json()['bookingid']
        patch_booking_response = auth_session.patch(f'{BASE_URL}/booking/{booking_id}', json=patch_data)
        assert patch_booking_response.status_code == 200, 'Данные не обновились'

        # Проверяем, что обновилось только то, что нужно
        patched_booking = auth_session.get(f'{BASE_URL}/booking/{booking_id}')
        assert patched_booking.json()['firstname'] == patch_data['firstname'], 'Имя не совпадает'
        assert patched_booking.json()['lastname'] == patch_data['lastname'], 'Фамилия не совпадает'

        assert patched_booking.json()['totalprice'] == booking_data['totalprice'], 'Обновились данные суммы, которые не должны были'
        assert patched_booking.json()['depositpaid'] == booking_data['depositpaid'], 'Обновились данные депозита, которые не должны были'
        assert patched_booking.json()['bookingdates'] == booking_data['bookingdates'], 'Обновились данные дат, которые не должны были'
        assert patched_booking.json()['bookingdates']['checkout'] == booking_data['bookingdates']['checkout'], 'Обновились данные даты выезда, которые не должны были'
        assert patched_booking.json()['bookingdates']['checkin'] == booking_data['bookingdates']['checkin'], 'Обновились данные даны заезда, которые не должны были'
        assert patched_booking.json()['additionalneeds'] == booking_data['additionalneeds'], 'Обновились данные доп услуг, которые не должны были'


    def test_incorrect_create(self, auth_session, missing_required_data):
        # Создаем бронирование с пропущенным обязательным полем
        created_booking_response = auth_session.post(f'{BASE_URL}/booking/', json=missing_required_data)
        assert created_booking_response.status_code != 200, 'Бронирование создалось без обязательного поля'

    def test_invalide_type_data_create(self, auth_session, invalid_type_data):
        # Создаем бронирование с пропущенным обязательным полем
        created_booking_response = auth_session.post(f'{BASE_URL}/booking/', json=invalid_type_data)
        assert created_booking_response.status_code != 200, 'Бронирование создалось с полем неправильного типа'

        response = auth_session.get(f'{BASE_URL}/booking/{created_booking_response.json()["bookingid"]}')
        print(response.json()) # bug: поле totalprice принял str

    def test_update_not_existed_resource(self, auth_session):
        # Получаем айдишники всех существующих ресурсов в виде списка словарей
        ids_lst = auth_session.get(f'{BASE_URL}/booking').json()

        # создаем множество существующих айдишинокв на основе списка
        ids_set = set()
        for e in ids_lst:
            ids_set.add(e['bookingid'])

        # Получаем несуществующий айдишник и кладем его в bookingid
        random_id = 1
        while random_id in ids_set:
            random_id = TestBookings.fake.random_int(1, 100)
            print("generated random_id", random_id)
        bookingid = random_id

        # Отправляем пут-запрос к ресурсу с этим несуществующим айдишником
        updated_response = auth_session.put(f'{BASE_URL}/booking/{bookingid}')

        # Проверяем, что данные обновить не удалось
        assert updated_response.status_code != 200, 'Обновились данные несуществующего ресурса'


    def test_unauthorized_delete(self, auth_session, booking_data):
        created_response = auth_session.post(f'{BASE_URL}/booking', json=booking_data)

        bookingid = created_response.json()['bookingid']

        deleted_response = requests.delete(f'{BASE_URL}/booking/{bookingid}')
        assert deleted_response.status_code == 403, 'Не получили Unauthorized Error'

    def test_patch_empty_data_booking(self, auth_session, booking_data, patch_empty_data):
        # Создаем бронирование и проверяем, что оно создалось
        created_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert created_booking.status_code == 200, "Ошибка при создании брони"

        #  Частично обновляем данные бронирования - имя и фамилию
        booking_id = created_booking.json()['bookingid']
        patch_booking_response = auth_session.patch(f'{BASE_URL}/booking/{booking_id}', json=patch_empty_data)
        assert patch_booking_response.status_code != 200, 'Данные обновились некорректно' # баг обновилось на пустые данные

