import requests
from url import Url
import allure

class TestOrderList:

    @allure.title('Получение списка заказов')
    @allure.description('Тест на получение успешного статуса')
    def test_order_list_status(self):
        response = requests.get(Url.order)
        assert response.status_code == 200

    @allure.title('Получение списка заказов')
    @allure.description('Тест на получение списка. (проверка длинны)')
    def test_order_list_check_len(self):
        response = requests.get(Url.order)
        assert len(response.json()['orders']) > 0
