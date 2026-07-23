import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from constants import Urls
from helpers.helpers import create_order_via_api, create_additional_order_via_api


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_counter_all_time_increases(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        token, order_number = create_order_via_api()

        main_page.open_page(Urls.BASE_URL)
        main_page.click_order_feed()
        initial_counter = order_feed_page.get_counter_all_time()

        create_additional_order_via_api(token)

        main_page.refresh_page()
        new_counter = order_feed_page.get_counter_all_time()
        assert new_counter > initial_counter

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
    def test_counter_today_increases(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        token, order_number = create_order_via_api()

        main_page.open_page(Urls.BASE_URL)
        main_page.click_order_feed()
        initial_counter = order_feed_page.get_counter_today()

        create_additional_order_via_api(token)

        main_page.refresh_page()
        new_counter = order_feed_page.get_counter_today()
        assert new_counter > initial_counter

    @allure.title("После оформления заказа его номер появляется в 'В работе'")
    def test_order_number_in_progress(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        token, order_number = create_order_via_api()

        main_page.open_page(Urls.BASE_URL)
        main_page.click_order_feed()

        order_in_progress = order_feed_page.get_order_number_in_progress()
        assert str(order_number) in order_in_progress



