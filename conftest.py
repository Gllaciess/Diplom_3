import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helpers.helpers import generate_random_user
from constants import Urls
from pages.locators import LoginPageLocators


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    user_data = generate_random_user()
    requests.post(Urls.REGISTER, data=user_data)

    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()

    login(driver, user_data)

    yield driver
    driver.quit()


def login(driver, user_data):
    "Вспомогательная функция для авторизации"
    from pages.main_page import MainPage
    
    main_page = MainPage(driver)
    main_page.open_page(Urls.LOGIN_PAGE)
    
    main_page.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
    main_page.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
    main_page.click_element(LoginPageLocators.LOGIN_BUTTON)


