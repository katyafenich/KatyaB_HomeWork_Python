from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.get("https://www.saucedemo.com/")

    def auth(self, username, password):
        # Ввести пароль и логин
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
