import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @allure.step("Закрыть модальное окно, если оно открыто")
    def close_modal_if_open(self):
        try:
            self.click_element(self.locators.CLOSE_BUTTON, timeout=3)
        except:
            pass

    @allure.step("Клик на 'Конструктор'")
    def click_constructor(self):
        self.close_modal_if_open()
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на 'Лента заказов'")
    def click_order_feed(self):
        self.close_modal_if_open()
        self.click_element(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_bun_ingredient(self):
        self.click_element(self.locators.BUN_INGREDIENT)

    @allure.step("Перетащить булку в конструктор")
    def drag_bun_to_constructor(self):
        if self.is_firefox:
            self.drag_and_drop_firefox(self.locators.BUN_INGREDIENT, self.locators.CONSTRUCTOR_TARGET)
        else:
            self.drag_and_drop(self.locators.BUN_INGREDIENT, self.locators.CONSTRUCTOR_TARGET)
        time.sleep(3)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click_element(self.locators.CLOSE_BUTTON)

    @allure.step("Получить счётчик ингредиента")
    def get_counter_value(self):
        return self.get_text(self.locators.COUNTER)

    @allure.step("Нажать 'Оформить заказ'")
    def click_order(self):
        self.click_element(self.locators.ORDER_BUTTON)


    @allure.step("Проверить, что модальное окно видимо")
    def is_modal_visible(self):
        "Проверяет, что модальное окно ингредиента отображается"
        return self.is_element_visible(self.locators.MODAL_WINDOW) is not None

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        "Проверяет, что модальное окно ингредиента закрыто"
        return self.is_element_invisible(self.locators.MODAL_WINDOW)


    