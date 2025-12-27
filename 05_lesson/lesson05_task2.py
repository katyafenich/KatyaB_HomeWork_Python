from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
button.click()

time.sleep(10)


driver.quit()
