from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 15, 0.1)


waiter.until(
    lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "#image-container img")) == 4
)


all_images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
print(f"Загружено картинок: {len(all_images)}")


src = all_images[2].get_attribute("src")
print(src)


driver.quit()