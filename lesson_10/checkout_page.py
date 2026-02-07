import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа
    """
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        Args:
            driver (WebDriver): объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Заполнить форму оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, zip_code):
        """
            Заполняет форму оформления заказа данными пользователя.

             Args:
                first_name (str): Имя покупателя
                last_name (str): Фамилия покупателя
                zip_code: Почтовый индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую стоимость заказа")
    def get_total_amount(self) -> str:
        """
        Получает итоговую стоимость заказа.
        Returns:
            str: Итоговая сумма заказа ($58.29)
        WebDriverWait:
            Ждет загрузки страницы с итогом
        """
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located
                ((By.CSS_SELECTOR, ".summary_total_label"))
        )
        total_text = (self.driver.find_element
                      (By.CSS_SELECTOR, ".summary_total_label").text)
        return total_text.replace("Total: $", "")

    @allure.step("Завершить оформление заказа")
    def finish_checkout(self):
        """
        Завершает оформление заказа нажатием кнопки Finish.
        """
        self.driver.find_element(By.ID, "finish").click()
