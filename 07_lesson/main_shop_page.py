from selenium.webdriver.common.by import By


class MainShopPage:
    def __init__(self, driver):
        self.driver = driver

    def add_cart(self):
        # Добавить в корзину нужные товары.
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
