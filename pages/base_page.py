import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.is_firefox = "firefox" in driver.capabilities["browserName"].lower()

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=10):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if self.is_firefox:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()
        return element

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти все элементы")
    def find_elements(self, locator, timeout=10):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    @allure.step("Получить URL текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step("Перетащить элемент (Firefox адаптация)")
    def drag_and_drop_firefox(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source)
        actions.move_to_element(target)
        actions.release()
        actions.perform()

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator, timeout=10):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except:
            return None

    @allure.step("Проверить невидимость элемента")
    def is_element_invisible(self, locator, timeout=10):
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except:
            return False

    @allure.step("Найти элемент по XPATH и вернуть его")
    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step("Отправить текст в поле")
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Кликнуть по элементу (без ожидания кликабельности)")
    def click_element_js(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)
    

