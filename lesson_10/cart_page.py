import allure
from selenium.webdriver.common.by import By


class CartPage:
    """
        Класс для работы со страницей корзины покупок.
    """
    def __init__(self, driver):
        """
                Инициализация страницы корзины.
                driver (WebDriver): объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Перейти к оформлению заказа")
    def go_to_checkout(self):
        """
        Нажимает кнопку для перехода к оформлению заказа.
        """
        self.driver.find_element(By.ID, "checkout").click()
