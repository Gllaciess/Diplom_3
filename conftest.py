import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helpers.helpers import generate_random_user, login_user_via_ui
from constants import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
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
    yield driver
    driver.quit()


@pytest.fixture
def auth_driver(driver):
    user_data = generate_random_user()
    requests.post(Urls.REGISTER, data=user_data)
    login_user_via_ui(driver, user_data)
    return driver


