import requests
from url import Url
import allure


class TestOrderList:

    @allure.title('Получение списка заказов')
    @allure.description('Тест на получение успешного статуса')
    def test_order_list_status(self):
        allure.dynamic.title("Получение списка заказов - Тест на успешный статус")
        allure.dynamic.description("Тест на получение успешного статуса")

        response = requests.get(Url.ORDER)
        assert response.status_code == 200

    @allure.title('Получение списка заказов')
    @allure.description('Тест на получение списка (проверка длины)')
    def test_order_list_check_len(self):
        allure.dynamic.title("Получение списка заказов - Тест на проверку длины")
        allure.dynamic.description("Тест на получение списка (проверка длины)")

        response = requests.get(Url.ORDER)
        assert len(response.json()['orders']) > 0
