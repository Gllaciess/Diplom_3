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
        self.is_firefox = "firefox" in self.driver.capabilities["browserName"].lower()

    @allure.step("Закрыть модальное окно, если оно открыто")
    def close_modal_if_open(self):
        try:
            self.click_element(self.locators.CLOSE_BUTTON)
        except:
            pass

    @allure.step("Клик на 'Конструктор'")
    def click_constructor(self):
        self.close_modal_if_open()
        if "firefox" in self.driver.capabilities["browserName"].lower():
            element = self.wait.until(EC.presence_of_element_located(self.locators.CONSTRUCTOR_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)
        else:
            self.click_element(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на 'Лента заказов'")
    def click_order_feed(self):
        self.close_modal_if_open()
        if "firefox" in self.driver.capabilities["browserName"].lower():
            element = self.wait.until(EC.presence_of_element_located(self.locators.ORDER_FEED_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)
        else:
            self.click_element(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_bun_ingredient(self):
        if "firefox" in self.driver.capabilities["browserName"].lower():
            element = self.wait.until(EC.presence_of_element_located(self.locators.BUN_INGREDIENT))
            self.driver.execute_script("arguments[0].click();", element)
        else:
            self.click_element(self.locators.BUN_INGREDIENT)

    @allure.step("Перетащить булку в конструктор")
    def drag_bun_to_constructor(self):
        if self.is_firefox:
            ingredient = self.driver.find_element(*self.locators.BUN_INGREDIENT)
            target = self.driver.find_element(*self.locators.CONSTRUCTOR_TARGET)
            actions = ActionChains(self.driver)
            actions.click_and_hold(ingredient)
            actions.move_to_element(target)
            actions.release()
            actions.perform()
            time.sleep(3)

        else:
            ingredient = self.driver.find_element(*self.locators.BUN_INGREDIENT)
            target = self.driver.find_element(*self.locators.CONSTRUCTOR_TARGET)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(ingredient, target).perform()

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        if "firefox" in self.driver.capabilities["browserName"].lower():
            element = self.wait.until(EC.presence_of_element_located(self.locators.CLOSE_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)
        else:
            self.click_element(self.locators.CLOSE_BUTTON)

    @allure.step("Получить счётчик ингредиента")
    def get_counter_value(self):
        value = self.get_text(self.locators.COUNTER)
        return value

    @allure.step("Нажать 'Оформить заказ'")
    def click_order(self):
        if "firefox" in self.driver.capabilities["browserName"].lower():
            element = self.wait.until(EC.presence_of_element_located(self.locators.ORDER_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)
        else:
            self.click_element(self.locators.ORDER_BUTTON)


