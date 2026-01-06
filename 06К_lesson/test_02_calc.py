import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_with_delay(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.CSS_SELECTOR, "#delay").click()

    driver.find_element(By.CSS_SELECTOR, ".keys span:nth-child(1)").click()  # 7
    driver.find_element(By.CSS_SELECTOR, ".keys span:nth-child(4)").click()  # +
    driver.find_element(By.CSS_SELECTOR, ".keys span:nth-child(2)").click()  # 8
    driver.find_element(By.CSS_SELECTOR, ".keys span:nth-child(15)").click()  # =

    wait = WebDriverWait(driver, 45)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15", f"Ожидался результат '15', но получено '{result}'"
