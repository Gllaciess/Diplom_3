import pytest
import random
import string
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def generate_random_user():
    def random_string(length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    return {
        "email": f"{random_string(8)}@test.com",
        "password": random_string(8),
        "name": random_string(6)
    }


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    # Создаём пользователя через API
    user_data = generate_random_user()
    requests.post('https://stellarburgers.education-services.ru/api/auth/register', data=user_data)

    # Запускаем браузер
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

    # Авторизуемся в браузере
    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(user_data["email"])
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(user_data["password"])
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    yield driver
    driver.quit()


    