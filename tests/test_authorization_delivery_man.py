import pytest
import requests
from url import Url
from helpers import Delivery
import allure


class TestAuthDelivery:

    @allure.title('Авторизация доставщика')
    @allure.description('проверка авторизации для зарегистрированного доставщика код ответа 200')
    def test_auth_delivery_man_success_status(self):
        payload = Delivery.registration_delivery_man(self)
        response = requests.post(Url.authorization_delivery_man, data=payload)
        Delivery.remove_delivery_man(payload)
        assert response.status_code == 200

    def test_auth_delivery_man_success_check_len_respons(self):
        payload = Delivery.registration_delivery_man(self)
        response = requests.post(Url.authorization_delivery_man, data=payload)
        Delivery.remove_delivery_man(payload)
        assert len(str(response.json().get('id'))) > 0

    def test_auth_delivery_account_not_exist_status(self):
        payload = Delivery.registration_delivery_man(self)
        response = requests.post(Url.authorization_delivery_man, data=payload)
        assert response.status_code == 400

    def test_auth_delivery_account_not_exist_message(self):
        payload = Delivery.registration_delivery_man(self)
        response = requests.post(Url.authorization_delivery_man, data=payload)
        assert response.json().get('message') == 'Учетная запись не найдена'

    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_auth_delivery_missing_login(self, field):
        payload = Delivery.registration_delivery_man(self)
        del payload[field]
        response = requests.post(Url.authorization_delivery_man, data=payload)
        assert response.status_code == 400 and response.json().get('message') == 'Недостаточно данных для входа'
