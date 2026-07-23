import allure
import pytest
from pages.main_page import MainPage
from constants import Urls


@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход на 'Конструктор'")
    def test_constructor_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_constructor()
        assert main_page.get_current_url() == Urls.BASE_URL

    @allure.title("Переход на 'Ленту заказов'")
    def test_order_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_order_feed()
        assert "/feed" in main_page.get_current_url()

    @allure.title("Открытие окна ингредиента")
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_bun_ingredient()
        assert main_page.is_element_visible(main_page.locators.MODAL_WINDOW) is not None

    @allure.title("Закрытие окна крестиком")
    def test_close_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_bun_ingredient()
        main_page.close_modal()
        assert main_page.is_element_invisible(main_page.locators.MODAL_WINDOW)

    @allure.title("Счётчик ингредиента увеличивается при добавлении")
    def test_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)

        initial_counter = main_page.get_counter_value()
        main_page.drag_bun_to_constructor()
        counter = main_page.get_counter_value()

        assert int(counter) > int(initial_counter)


