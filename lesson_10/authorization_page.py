import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AuthPage:
    """
        Класс для работы со страницей авторизации.

        Attributes:
            driver: WebDriver — объект драйвера Selenium
            wait: WebDriverWait - объект для явных ожиданий
    """
    def __init__(self, driver):
        """
                Инициализация страницы авторизации.

                Args:
                 driver: WebDriver - объект драйвера Selenium
         """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация пользователя {username}")
    def auth(self, username: str, password: str):
        """
                Выполняет авторизацию пользователя.

                Args:
                 username: str - имя пользователя
                 password: str - пароль пользователя
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
