from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        first_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='first-name']")))
        first_name.send_keys("Иван")

        last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
        last_name.send_keys("Петров")

        address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
        address.send_keys("Ленина, 55-3")

        email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
        email.send_keys("test@skypro.com")

        phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        phone.send_keys("+7985899998787")

        city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
        city.send_keys("Москва")

        country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
        country.send_keys("Россия")

        job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
        job_position.send_keys("QA")

        company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
        company.send_keys("SkyPro")

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

        zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
        zip_code_classes = zip_code_field.get_attribute("class")

        assert "is-invalid" in zip_code_classes or "danger" in zip_code_classes, \
            f"Поле Zip code не подсвечено красным. Классы: {zip_code_classes}"

        fields_to_check = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]

        for field_name in fields_to_check:
            field = driver.find_element(By.CSS_SELECTOR, f"#{field_name}")
            field_classes = field.get_attribute("class")

            assert "is-valid" in field_classes or "success" in field_classes, \
                f"Поле {field_name} не подсвечено зеленым. Классы: {field_classes}"

        print("Все проверки пройдены успешно!")

    finally:
        driver.quit()
