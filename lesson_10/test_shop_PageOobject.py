import allure
import pytest
from selenium import webdriver
from authorization_page import AuthPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера Firefox.
    """
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полное оформление заказа в магазине")
@allure.description("""
Тест проверяет полный процесс покупки в интернет-магазине.
Шаги:
1. Авторизация пользователя
2. Добавление товаров в корзину
3. Переход к оформлению заказа
4. Заполнение данных для доставки
5. Проверка итоговой суммы
6. Завершение оформления
""")
def test_complete_purchase(driver):
    """
    Тестирование полного процесса оформления заказа.
    """
    with allure.step("Авторизация пользователя"):
        auth = AuthPage(driver)
        auth.auth("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        main_page = MainShopPage(driver)
        main_page.add_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.go_to_checkout()

    with allure.step("Заполнение формы оформления"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form("Люблю", "Мир", "123456")

    with allure.step("Проверка итоговой суммы"):
        total_amount = checkout_page.get_total_amount()
        expected_total = "58.29"
    assert total_amount == expected_total, \
        f"Итоговая сумма {total_amount} не равна ожидаемой {expected_total}"

    print(f"Тест пройден успешно! Итоговая сумма: ${total_amount}")

    with allure.step("Завершение оформления заказа"):
        checkout_page.finish_checkout()
