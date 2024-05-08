import pytest
import requests
from url import Url
from helpers import Delivery
import allure


class TestAuthDelivery:

    @allure.title('Авторизация доставщика')
    @allure.description('проверка авторизации для зарегистрированного доставщика код ответа 200')
    def test_auth_delivery_man_success_status(self):
        # Создание доставщика и получение данных для авторизации
        payload = Delivery.generation_register_data_delivery_man()

        # Регистрация доставщика
        Delivery.registration_delivery_man(payload)

        # Авторизация доставщика
        response = requests.post(Url.authorization_delivery_man, data=payload)

        # Удаление доставщика
        Delivery.remove_delivery_man(payload)

        # Проверка успешной авторизации
        assert response.status_code == 200

    def test_auth_delivery_man_success_check_len_response(self):
        # Создание доставщика и получение данных для авторизации
        payload = Delivery.generation_register_data_delivery_man()

        # Регистрация доставщика
        Delivery.registration_delivery_man(payload)

        # Авторизация доставщика
        response = requests.post(Url.authorization_delivery_man, data=payload)

        # Удаление доставщика
        Delivery.remove_delivery_man(payload)

        # Проверка длины ответа
        assert len(str(response.json().get('id', ''))) > 0

    def test_auth_delivery_account_not_exist_status(self):
        # Создание доставщика и получение данных для авторизации
        payload = Delivery.generation_register_data_delivery_man()

        # Авторизация доставщика с неверными данными
        response = requests.post(Url.authorization_delivery_man, data=payload)

        # Проверка статуса 404, так как учетная запись не существует
        assert response.status_code == 404

    def test_auth_delivery_account_not_exist_message(self):
        # Создание доставщика и получение данных для авторизации
        payload = Delivery.generation_register_data_delivery_man()

        # Авторизация доставщика с неверными данными
        response = requests.post(Url.authorization_delivery_man, data=payload)

        # Проверка сообщения об ошибке
        assert response.json().get('message') == 'Учетная запись не найдена'

    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_auth_delivery_missing_login(self, field):
        # Создание доставщика и получение данных для авторизации
        payload = Delivery.generation_register_data_delivery_man()

        # Регистрация доставщика
        Delivery.registration_delivery_man(payload)

        # Удаление одного из обязательных полей из данных для авторизации
        invalid_payload = payload.copy()
        del invalid_payload[field]

        # Авторизация доставщика с неполными данными
        response = requests.post(Url.authorization_delivery_man, data=invalid_payload)

        # Проверка статуса 400 и сообщения об ошибке
        assert response.status_code == 400 and response.json().get('message') == 'Недостаточно данных для входа'
