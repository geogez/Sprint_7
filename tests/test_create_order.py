import json
import pytest
from url import Url
from data import Order
import requests
import allure

class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('тест получения успешного статуса')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order_status_code(self, color):
        payload = Order.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = requests.post(Url.order, payload)
        assert response.status_code == 201

    @allure.title('Создание заказа')
    @allure.description('тест статуса заказа, больше нуля')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order_len_respons(self, color):
        payload = Order.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = requests.post(Url.order, payload)
        assert len(str(response.json()['track'])) > 0
