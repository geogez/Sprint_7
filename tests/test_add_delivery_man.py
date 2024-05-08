import json
import requests
import pytest
import allure
from url import Url
from helpers import Delivery


class TestAddDelivery:

    @allure.title('Успешное создание доставщика')
    def test_add_delivery_status(self):
        # Создание доставщика
        payload = Delivery.generation_register_data_delivery_man()
        response = requests.post(Url.create_delivery_man, json=payload)
        Delivery.remove_delivery_man(payload)

        # Проверка успешного создания
        assert response.status_code == 201 and response.json().get('ok') == True

    @allure.title('Тест на создание доставщика с теми же данными')
    def test_add_delivery_man_repeated_data_registration_status(self):
        # Создание доставщика с теми же данными
        payload = Delivery.generation_register_data_delivery_man()
        requests.post(Url.create_delivery_man, json=payload)
        response = requests.post(Url.create_delivery_man, json=payload)
        Delivery.remove_delivery_man(payload)

        # Проверка статуса 409 и сообщения об ошибке
        assert response.status_code == 409 and response.json().get(
            'message') == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание доставщика используя не все обязательные поля')
    @pytest.mark.parametrize('field', ['login', 'password', 'firstName'])
    def test_delivery_man_invalid_field(self, field):
        # Создание доставщика с отсутствующим обязательным полем
        payload = Delivery.generation_register_data_delivery_man()
        del payload[field]
        response = requests.post(Url.create_delivery_man, json=payload)

        # Проверка статуса кода ответа
        assert response.status_code == 400

        # Проверка сообщения об ошибке
        assert response.json().get('message') == 'Недостаточно данных для создания учетной записи'
