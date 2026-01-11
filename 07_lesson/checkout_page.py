from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_form(self, first_name, last_name, zip_code):
        # Заполнить форму оформления заказа
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self):
        # Получить итоговую стоимость
        # Ждем загрузки страницы с итогом
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        total_text = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        # Извлекаем сумму из строки "Total: $58.29"
        return total_text.replace("Total: $", "")

    def finish_checkout(self):
        # Завершить оформление заказа
        self.driver.find_element(By.ID, "finish").click()
