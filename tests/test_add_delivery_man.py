import pytest
import allure
import requests
from url import Url
from helpers import Delivery


class TestAddDelivery:

    @allure.title('Создание доставщика')
    @allure.description('Проверка успешного создания доставщика')
    def test_add_delivery_status(self, registered_delivery_payload):
        allure.dynamic.title("Создание доставщика - Успешное создание")
        allure.dynamic.description("Проверка успешного создания доставщика")

        response = requests.post(Url.CREATE_DELIVERY_MAN, json=registered_delivery_payload)
        assert response.status_code == 201 and response.json().get('ok') == True

    @allure.title('Создание доставщика')
    @allure.description('Тест на создание доставщика с теми же данными')
    def test_add_delivery_man_repeated_data_registration_status(self, registered_delivery_payload):
        allure.dynamic.title("Создание доставщика - Проверка повторной регистрации")
        allure.dynamic.description("Тест на создание доставщика с теми же данными")

        requests.post(Url.CREATE_DELIVERY_MAN, json=registered_delivery_payload)
        response = requests.post(Url.CREATE_DELIVERY_MAN, json=registered_delivery_payload)
        assert response.status_code == 409 and response.json().get(
            'message') == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание доставщика')
    @allure.description('Создание доставщика используя не все обязательные поля')
    @pytest.mark.parametrize('field', ['login', 'password', 'firstName'])
    def test_delivery_man_invalid_field(self, field, registered_delivery_payload):
        allure.dynamic.title("Создание доставщика - Использование не всех обязательных полей")
        allure.dynamic.description("Создание доставщика используя не все обязательные поля")

        payload = registered_delivery_payload.copy()
        del payload[field]
        response = requests.post(Url.CREATE_DELIVERY_MAN, json=payload)
        assert response.status_code == 400
        assert response.json().get('message') == 'Недостаточно данных для создания учетной записи'
