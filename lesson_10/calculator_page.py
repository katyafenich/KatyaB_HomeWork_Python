import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
       Класс для работы со страницей калькулятора.

       Attributes:
           driver (WebDriver): объект драйвера Selenium
           wait (WebDriverWait): Объект для явных ожиданий
           button_locators: Словарь с локаторами кнопок
    """
    def __init__(self, driver):
        """
                Инициализация страницы калькулятора.

                Args:
                 driver (WebDriver): объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        # Локаторы.
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        # Кнопки
        self.button_locators = {
            '0': (By.XPATH, "//span[text()='0']"),
            '1': (By.XPATH, "//span[text()='1']"),
            '2': (By.XPATH, "//span[text()='2']"),
            '3': (By.XPATH, "//span[text()='3']"),
            '4': (By.XPATH, "//span[text()='4']"),
            '5': (By.XPATH, "//span[text()='5']"),
            '6': (By.XPATH, "//span[text()='6']"),
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '9': (By.XPATH, "//span[text()='9']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '-': (By.XPATH, "//span[text()='-']"),
            '×': (By.XPATH, "//span[text()='×']"),
            '÷': (By.XPATH, "//span[text()='÷']"),
            '=': (By.XPATH, "//span[text()='=']"),
            'C': (By.XPATH, "//span[text()='C']")
        }

    @allure.step("Открыть страницу калькулятора: {url}")
    def open(self, url: str):
        """
         Открывает указанный URL в браузере.
         Args:
            url (str): URL страницы калькулятора
        """
        self.driver.get(url)

    @allure.step("Установить задержку: {delay_value} секунд")
    def set_delay(self, delay_value: int):
        """
            Устанавливает значение задержки вычислений.

            Args:
                delay_value (int): Задержка в секундах
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    @allure.step("Нажать кнопку: {button}")
    def click_button(self, button):
        """
               Нажимает указанную кнопку калькулятора.

               Args:
                   button: Символ кнопки для нажатия
        """
        locator = self.button_locators.get(button)
        if locator:
            button_element = self.driver.find_element(*locator)
            button_element.click()

    @allure.step("Ввести выражение: {expression}")
    def enter_calculation(self, expression: str):
        """
               Вводит последовательность кнопок для вычисления выражения.

               Args:
                   expression (str): Выражение для вычисления
        """
        for char in expression:
            self.click_button(char)

    @allure.step("Получить результат с дисплея")
    def get_result(self) -> str:
        """
            Получает текущее значение с дисплея калькулятора.

            Returns:
                str: Текущее значение на дисплее
        """
        result_element = self.driver.find_element(*self.result_display)
        return result_element.text

    @allure.step("Ожидание результата: {expected_result}")
    def wait_for_result(self, expected_result: str, timeout: int = 50) -> str:
        """
        Ожидает появления указанного результата на дисплее.

        Args:
            expected_result (str): Ожидаемый результат
            timeout (int): Максимальное время ожидания в секундах

        Returns:
            str: Фактический результат с дисплея
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element
            (self.result_display, expected_result)
        )
        return self.get_result()
