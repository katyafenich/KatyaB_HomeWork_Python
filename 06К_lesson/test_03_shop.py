import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
    )
    username.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("secret_sauce")

    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list"))
    )

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_info_container"))
    )

    first_name_input = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name_input.send_keys("Катя")

    last_name_input = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name_input.send_keys("PythonЖесть")

    postal_code_input = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code_input.send_keys("123456")

    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_button.click()

    total_label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
    )

    total_text = total_label.text

    assert total_text == "Total: $58.29", f"Ожидалась сумма $58.29, но получено: {total_text}"
