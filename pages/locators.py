from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    BUN_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter__')]//p[contains(@class, 'counter_counter__num__')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    CONSTRUCTOR_TARGET = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__')]")


class OrderFeedPageLocators:
    ORDER_FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")
    
    @staticmethod
    def get_order_feed_item(order_number):
        return (By.XPATH, f"//a[contains(@href, '/feed/{order_number}')]")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


