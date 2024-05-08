from url import Url
from helpers import Delivery
import requests
import pytest
import allure


class TestAddDelivery:

    @allure.title('Успешное создание доставщика')
    def test_add_delivery_status(self):
        payload = Delivery.generation_register_data_delivery_man(self)
        response = requests.post(Url.create_delivery_man, data=payload)
        Delivery.remove_delivery_man(payload)
        assert response.status_code == 201 and response.json().get('ok') == True

    @allure.title('Тест на создание доставщика с теми же данными')
    def test_add_delivery_man_repeated_data_registration_status(self):
        payload = Delivery.generation_register_data_delivery_man(self)
        requests.post(Url.create_delivery_man, data=payload)
        response = requests.post(Url.create_delivery_man, data=payload)
        Delivery.remove_delivery_man(payload)
        assert response.status_code == 409 and response.json().get('message') == 'Этот логин уже используется. Попробуйте другой.'


    @allure.title('Создание доставщика используя не все обязательные поля')
    @pytest.mark.parametrize('field', ['login', 'password', 'firstName'])
    def test_delivery_man_invalid_field(self, field):
        payload = Delivery.generation_register_data_delivery_man(self)
        del payload[field]
        response = requests.post(Url.create_delivery_man, data=payload)
        assert response.status_code == 400 and response.json().get('message') == 'Недостаточно данных для создания учетной записи'

