import pytest
from selenium import webdriver
from authorization_page import AuthPage
from maine_shop_page import MaineShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_complete_purchase():
    driver = webdriver.Firefox()
    auth = AuthPage(driver)
    auth.auth("standard_user", "secret_sauce")

    maine_page = MaineShopPage(driver)
    maine_page.add_cart()

    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Люблю", "Мир", "123456")
    total_amount = checkout_page.get_total_amount()

    expected_total = "58.29"
    assert total_amount == expected_total, \
        f"Итоговая сумма {total_amount} не равна ожидаемой {expected_total}"

    print(f"Тест пройден успешно! Итоговая сумма: ${total_amount}")

    checkout_page.finish_checkout()
