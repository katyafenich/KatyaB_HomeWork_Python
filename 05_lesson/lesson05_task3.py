from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")


search_box = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_box.send_keys("Sky")

time.sleep(3)


search_box.clear()

time.sleep(3)
search_box.send_keys("Pro")
driver.quit()
