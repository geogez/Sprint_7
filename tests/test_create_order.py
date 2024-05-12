import pytest
import json
import requests
from url import Url
from data import Order
import allure


class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('Проверка получения успешного статуса')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order_status_code(self, color, registered_delivery_payload):
        allure.dynamic.title("Создание заказа - Проверка успешного статуса")
        allure.dynamic.description("Проверка получения успешного статуса")

        # Авторизация доставщика
        response = requests.post(Url.AUTHORIZATION_DELIVERY_MAN, data=registered_delivery_payload)

        payload = Order.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = requests.post(Url.ORDER, payload)

        assert response.status_code == 201

    @allure.title('Создание заказа')
    @allure.description('Проверка статуса заказа больше нуля')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order_len_response(self, color, registered_delivery_payload):
        allure.dynamic.title("Создание заказа - Проверка статуса больше нуля")
        allure.dynamic.description("Проверка статуса заказа больше нуля")

        # Авторизация доставщика
        response = requests.post(Url.AUTHORIZATION_DELIVERY_MAN, data=registered_delivery_payload)

        payload = Order.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = requests.post(Url.ORDER, payload)

        assert len(str(response.json()['track'])) > 0
