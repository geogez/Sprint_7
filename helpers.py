import requests
import random
import string
from url import Url
import allure

class Delivery:

    @staticmethod
    @allure.step("Генератор инфо для регистрации доставщика")
    def generation_register_data_delivery_man():
        def generation_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generation_random_string(10)
        password = generation_random_string(10)
        first_name = generation_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}

        return payload

    @staticmethod
    @allure.step("Регистрация доставщика")
    def registration_delivery_man(payload):  # Передаем payload в качестве аргумента
        response = requests.post(Url.create_delivery_man, json=payload)  # Использование json вместо data
        return response

    @staticmethod
    @allure.step("Удаление инфо о доставщике")
    def remove_delivery_man(payload):  # Добавлен параметр payload
        response = requests.post(Url.authorization_delivery_man, json=payload)  # Использование json вместо data
        delivery_man_id = response.json().get("id")
        if delivery_man_id:  # Проверяем наличие ID перед отправкой запроса на удаление
            requests.delete(f'{Url.create_delivery_man}/{delivery_man_id}')
