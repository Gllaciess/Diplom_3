import random
import string
import requests
from constants import Urls


def generate_random_user():
    def random_string(length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    return {
        "email": f"{random_string(8)}@test.com",
        "password": random_string(8),
        "name": random_string(6)
    }


def create_order_via_api():
    "Создаёт пользователя, логинится и создаёт заказ"
    user = generate_random_user()
    
    # Регистрация
    requests.post(Urls.REGISTER, data=user)
    
    # Логин
    login_response = requests.post(Urls.LOGIN, data={
        'email': user['email'],
        'password': user['password']
    })
    token = login_response.json().get('accessToken')
    
    # Создание заказа
    order_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
    response = requests.post(
        Urls.ORDERS,
        json=order_data,
        headers={'Authorization': token}
    )
    order_number = response.json().get('order', {}).get('number')
    
    return token, order_number


def create_additional_order_via_api(token):
    "Создаёт дополнительный заказ для проверки счётчиков"
    order_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
    response = requests.post(
        Urls.ORDERS,
        json=order_data,
        headers={'Authorization': token}
    )
    return response.json().get('order', {}).get('number')


