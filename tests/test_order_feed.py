import allure
import requests
import random
import string
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
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
    # Создаёт пользователя, логинится и создаёт заказ
    user = generate_random_user()
    requests.post('https://stellarburgers.education-services.ru/api/auth/register', data=user)

    login_response = requests.post('https://stellarburgers.education-services.ru/api/auth/login', data={
        'email': user['email'],
        'password': user['password']
    })
    token = login_response.json().get('accessToken')

    order_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }
    response = requests.post(
        'https://stellarburgers.education-services.ru/api/orders',
        json=order_data,
        headers={'Authorization': token}
    )
    order_number = response.json().get('order', {}).get('number')
    
    return token, order_number


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_counter_all_time_increases(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        token, order_number = create_order_via_api()

        driver.get(Urls.BASE_URL)
        main_page.click_order_feed()
        initial_counter = order_feed_page.get_counter_all_time()

        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        requests.post(
            'https://stellarburgers.education-services.ru/api/orders',
            json=order_data,
            headers={'Authorization': token}
        )

        driver.refresh()
        new_counter = order_feed_page.get_counter_all_time()
        assert new_counter > initial_counter

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
    def test_counter_today_increases(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        token, order_number = create_order_via_api()

        driver.get(Urls.BASE_URL)
        main_page.click_order_feed()
        initial_counter = order_feed_page.get_counter_today()

        order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        requests.post(
            'https://stellarburgers.education-services.ru/api/orders',
            json=order_data,
            headers={'Authorization': token}
        )

        driver.refresh()
        new_counter = order_feed_page.get_counter_today()
        assert new_counter > initial_counter

    @allure.title("После оформления заказа в 'В работе'")
    def test_order_number_in_progress(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        token, order_number = create_order_via_api()

        driver.get(Urls.BASE_URL)
        main_page.click_order_feed()

        order_in_progress = order_feed_page.get_order_number_in_progress()
        assert str(order_number) in order_in_progress


