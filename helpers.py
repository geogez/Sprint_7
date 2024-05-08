import requests
import random
import string
from url import Url
import allure

class Delivery:

    @allure.step("Генератор инфо для регистрации доставщика")
    def generation_register_data_delivery_man(self):
        def generation_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generation_random_string(10)
        password = generation_random_string(10)
        first_name = generation_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}

        return payload

    @allure.step("Регистрация доставщика")
    def registration_delivery_man(self):
        payload = Delivery.generation_register_data_delivery_man
        response = requests.post(Url.create_delivery_man, data=payload)
        return payload

    @allure.step("Удаление инфо о доставщике")
    def remove_delivery_man(data):
        payload = data
        respons = requests.post(Url.authorization_delivery_man, data=payload)
        delivery_man_id = respons.json()["id"]
        requests.delete(f'{Url.create_delivery_man}/{delivery_man_id}')
