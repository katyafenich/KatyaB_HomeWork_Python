import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)

    (calculator_page.open
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"))

    calculator_page.set_delay(45)

    calculator_page.enter_calculation("7+8=")

    result = calculator_page.wait_for_result("15")

    assert result == "15", f"Ожидался результат 15, но получили {result}"
