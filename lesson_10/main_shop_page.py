import allure
from selenium.webdriver.common.by import By


class MainShopPage:
    """
    Класс для работы с главной страницей магазина.
    """
    def __init__(self, driver):
        """
            Инициализация главной страницы магазина.

            Args:
                driver (WebDriver): объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Добавить товары в корзину")
    def add_cart(self):
        """
        Добавляет предопределенные товары в корзину.
        """
        (self.driver.find_element
         (By.ID, "add-to-cart-sauce-labs-backpack").click())
        (self.driver.find_element
         (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click())
        (self.driver.find_element
         (By.ID, "add-to-cart-sauce-labs-onesie").click())
        (self.driver.find_element
         (By.CSS_SELECTOR, ".shopping_cart_link").click())
