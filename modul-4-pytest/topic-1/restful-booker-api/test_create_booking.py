import pytest
import requests
from faker import Faker
from constants import BASE_URL
import copy

class TestBookings:
    fake = Faker()

    def test_unauthorized_delete(self, requester_with_auth_session, booking_data):
        created_response = requester_with_auth_session.send_request(
            method='POST',
            endpoint='/booking',
            data=booking_data
        )

        bookingid = created_response.json()['bookingid']

        copied_requester = copy.deepcopy(requester_with_auth_session)
        copied_requester._update_session_headers(**{'Cookie': None})
        deleted_response = copied_requester.send_request(
            method='DELETE',
            endpoint=f'/booking/{bookingid}',
            expected_status=403,
        )

    def test_create_booking(self, requester_with_auth_session, booking_data):
        # Создаём бронирование
        create_booking = requester_with_auth_session.send_request(method='POST', endpoint= "/booking", data=booking_data)


        booking_id = create_booking.json().get('bookingid')
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"

        # Проверяем, что бронирование можно получить по ID
        get_booking = requester_with_auth_session.send_request(
            method='GET',
            endpoint=f"/booking/{booking_id}"
        )
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        # Удаляем бронирование
        deleted_booking = requester_with_auth_session.send_request(
            method='DELETE',
            endpoint=f"/booking/{booking_id}",
            expected_status=201
        )

        # Проверяем, что бронирование больше недоступно
        get_booking = requester_with_auth_session.send_request(
            method='GET',
            endpoint=f"/booking/{booking_id}",
            expected_status=404
        )


    def test_update_booking(self, requester_with_auth_session, booking_data, put_data):
        # Создаем бронирование и проверяем, что оно создалось
        create_booking = requester_with_auth_session.send_request(
            method='POST',
            endpoint='/booking',
            data=booking_data
        )

        # Обновляем данные бронирования
        booking_id = create_booking.json()['bookingid']
        put_booking_response = requester_with_auth_session.send_request(
            method='PUT',
            endpoint=f'/booking/{booking_id}',
            data=put_data
        )

        # Проверяем, что данные действительно обновились
        updated_booking = requester_with_auth_session.send_request(
            method='GET',
            endpoint=f'/booking/{booking_id}'
        )
        assert updated_booking.json() == put_data, 'Измененные данные не совпадают'


    def test_patch_booking(self, requester_with_auth_session, booking_data, patch_data):
        # Создаем бронирование и проверяем, что оно создалось
        created_booking = requester_with_auth_session.send_request(
            method='POST',
            endpoint="/booking",
            data=booking_data
        )

        #  Частично обновляем данные бронирования - имя и фамилию
        booking_id = created_booking.json()['bookingid']
        patch_booking_response = requester_with_auth_session.send_request(
            method='PATCH',
            endpoint=f'/booking/{booking_id}',
            data=patch_data
        )

        # Проверяем, что обновилось только то, что нужно
        patched_booking = requester_with_auth_session.send_request(
            method='GET',
            endpoint=f'/booking/{booking_id}'
        )
        assert patched_booking.json()['firstname'] == patch_data['firstname'], 'Имя не совпадает'
        assert patched_booking.json()['lastname'] == patch_data['lastname'], 'Фамилия не совпадает'

        assert patched_booking.json()['totalprice'] == booking_data['totalprice'], 'Обновились данные суммы, которые не должны были'
        assert patched_booking.json()['depositpaid'] == booking_data['depositpaid'], 'Обновились данные депозита, которые не должны были'
        assert patched_booking.json()['bookingdates'] == booking_data['bookingdates'], 'Обновились данные дат, которые не должны были'
        assert patched_booking.json()['bookingdates']['checkout'] == booking_data['bookingdates']['checkout'], 'Обновились данные даты выезда, которые не должны были'
        assert patched_booking.json()['bookingdates']['checkin'] == booking_data['bookingdates']['checkin'], 'Обновились данные даны заезда, которые не должны были'
        assert patched_booking.json()['additionalneeds'] == booking_data['additionalneeds'], 'Обновились данные доп услуг, которые не должны были'


    def test_incorrect_create(self, requester_with_auth_session, missing_required_data):
        # Создаем бронирование с пропущенным обязательным полем
        created_booking_response = requester_with_auth_session.send_request(
            method='POST',
            endpoint='/booking/',
            data=missing_required_data,
            expected_status=500 # баг? код 500 на неправильный запрос
        )

    def test_invalide_type_data_create(self, requester_with_auth_session, invalid_type_data):
        # Создаем бронирование с неправильным типом данных в totalprice (str вместо int)
        created_booking_response = requester_with_auth_session.send_request(
            method='POST',
            endpoint='/booking/',
            data=invalid_type_data,
            expected_status=400 # баг. в поле totalprice принял str.
        )


    def test_update_not_existed_resource(self, requester_with_auth_session):
        # Получаем айдишники всех существующих ресурсов в виде списка словарей
        ids_lst = requester_with_auth_session.send_request(method='GET', endpoint='/booking', need_logging=False).json()

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
        updated_response = requester_with_auth_session.send_request(
            method='PUT',
            endpoint=f'/booking/{bookingid}',
            expected_status=400
        )



    def test_patch_empty_data_booking(self, requester_with_auth_session, booking_data, patch_empty_data):
        # Создаем бронирование и проверяем, что оно создалось
        created_booking = requester_with_auth_session.send_request(
            method='POST',
            endpoint="/booking",
            data=booking_data
        )

        #  Частично обновляем данные бронирования - имя и фамилию
        booking_id = created_booking.json()['bookingid']
        patch_booking_response = requester_with_auth_session.send_request(
            method='PATCH',
            endpoint=f'/booking/{booking_id}',
            data=patch_empty_data,
            expected_status=400 # баг обновилось на пустые данные
        )

