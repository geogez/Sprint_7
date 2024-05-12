import pytest
import requests
from url import Url
from helpers import Delivery
import allure


class TestAuthDelivery:

    @allure.title('Авторизация доставщика')
    @allure.description('Проверка авторизации для зарегистрированного доставщика, код ответа 200')
    def test_auth_delivery_man_success_status(self, registered_delivery_payload):
        allure.dynamic.title("Авторизация доставщика - Проверка успешного статуса")
        allure.dynamic.description("Проверка авторизации для зарегистрированного доставщика, ожидаемый код ответа 200")

        response = requests.post(Url.authorization_delivery_man, data=registered_delivery_payload)
        assert response.status_code == 200

    @allure.title('Авторизация доставщика')
    @allure.description('Проверка успешного возврата идентификатора при успешной авторизации')
    def test_auth_delivery_man_success_check_len_response(self, registered_delivery_payload):
        allure.dynamic.title("Авторизация доставщика - Проверка успешного возврата идентификатора")
        allure.dynamic.description("Проверка успешного возврата идентификатора доставщика при успешной авторизации")

        response = requests.post(Url.AUTHORIZATION_DELIVERY_MAN, data=registered_delivery_payload)
        assert len(str(response.json().get('id', ''))) > 0

    @allure.title('Авторизация доставщика')
    @allure.description('Проверка статуса 404 при попытке авторизации с несуществующей учетной записью')
    def test_auth_delivery_account_not_exist_status(self):
        allure.dynamic.title("Авторизация доставщика - Проверка статуса 404")
        allure.dynamic.description("Проверка статуса 404 при попытке авторизации с несуществующей учетной записью")

        payload = Delivery.generation_register_data_delivery_man()
        response = requests.post(Url.AUTHORIZATION_DELIVERY_MAN, data=payload)
        assert response.status_code == 404

    @allure.title('Авторизация доставщика')
    @allure.description('Проверка сообщения об ошибке при попытке авторизации с несуществующей учетной записью')
    def test_auth_delivery_account_not_exist_message(self):
        allure.dynamic.title("Авторизация доставщика - Проверка сообщения об ошибке")
        allure.dynamic.description(
            "Проверка сообщения об ошибке при попытке авторизации с несуществующей учетной записью")

        payload = Delivery.generation_register_data_delivery_man()
        response = requests.post(Url.AUTHORIZATION_DELIVERY_MAN, data=payload)
        assert response.json().get('message') == 'Учетная запись не найдена'

    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_auth_delivery_missing_login(self, field, registered_delivery_payload):
        allure.dynamic.title("Авторизация доставщика - Проверка отсутствия обязательного поля")
        allure.dynamic.description(
            "Проверка статуса 400 и сообщения об ошибке при попытке авторизации с отсутствующим обязательным полем")

        invalid_payload = registered_delivery_payload.copy()
        del invalid_payload[field]
        response = requests.post(Url.AUTHORIZATION_DELIVERY_MAN, data=invalid_payload)
        assert response.status_code == 400 and response.json().get('message') == 'Недостаточно данных для входа'
