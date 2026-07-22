import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators

    @allure.step("Проверить, что страница ленты заказов открыта")
    def is_order_feed_page_opened(self):
        return self.wait.until(EC.visibility_of_element_located(self.locators.ORDER_FEED_HEADER)).is_displayed()

    @allure.step("Получить счётчик 'Выполнено за всё время'")
    def get_counter_all_time(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.COUNTER_ALL_TIME))
        return int(self.get_text(self.locators.COUNTER_ALL_TIME))

    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_counter_today(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.COUNTER_TODAY))
        return int(self.get_text(self.locators.COUNTER_TODAY))

    @allure.step("Найти номер заказа в ленте")
    def get_order_number_in_feed(self, order_number):
        locator = (By.XPATH, f"//a[contains(@href, '/feed/{order_number}')]")
        return len(self.driver.find_elements(*locator)) > 0
    
    @allure.step("Получить номер заказа в работе")
    def get_order_number_in_progress(self):
        locator = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")
        return self.get_text(locator)
    

    