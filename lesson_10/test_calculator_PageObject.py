import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест вычисления 7 + 8 с задержкой")
@allure.description("""
    Тест проверяет работу калькулятора с задержкой вычислений.
    Шаги:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Ввести выражение 7+8=
    4. Дождаться результата 15
    5. Проверить корректность вычислений
    """)
def test_calculator(driver):
    """
    Тестирование работы калькулятора с задержкой.
    """
    calculator_page = CalculatorPage(driver)

    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay(45)

    with allure.step("Выполнить вычисление 7 + 8"):
        calculator_page.enter_calculation("7+8=")

    with allure.step("Дождаться результата"):
        result = calculator_page.wait_for_result("15")

    with allure.step("Проверить результат вычисления"):
        assert result == "15", (
            f"Ожидался результат 15, но получили {result}"
        )
