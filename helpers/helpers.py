import random
import string
import requests
from constants import Urls

INGREDIENT_IDS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]


def generate_random_user():
    def random_string(length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    return {
        "email": f"{random_string(8)}@yandex.ru",
        "password": random_string(8),
        "name": random_string(6)
    }


# Создаёт пользователя, логинится и создаёт заказ
def create_order_via_api():
    user = generate_random_user()
    
    # Регистрация
    register_response = requests.post(Urls.REGISTER, data=user)
    register_response.raise_for_status()
    
    # Логин
    login_response = requests.post(Urls.LOGIN, data={
        'email': user['email'],
        'password': user['password']
    })
    login_response.raise_for_status()
    token = login_response.json().get('accessToken')
    
    # Создание заказа
    order_data = {"ingredients": INGREDIENT_IDS}
    response = requests.post(
        Urls.ORDERS,
        json=order_data,
        headers={'Authorization': token}
    )
    response.raise_for_status()
    order_number = response.json().get('order', {}).get('number')
    return token, order_number


# Создаёт дополнительный заказ для проверки счётчиков
def create_additional_order_via_api(token):
    order_data = {"ingredients": INGREDIENT_IDS}
    response = requests.post(
        Urls.ORDERS,
        json=order_data,
        headers={'Authorization': token}
    )
    response.raise_for_status()
    return response.json().get('order', {}).get('number')


def login_user_via_ui(driver, user_data):
    "Авторизует пользователя через UI"
    from pages.main_page import MainPage
    from pages.locators import LoginPageLocators
    from constants import Urls
    
    main_page = MainPage(driver)
    main_page.open_page(Urls.LOGIN_PAGE)
    main_page.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
    main_page.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
    main_page.click_element(LoginPageLocators.LOGIN_BUTTON)


