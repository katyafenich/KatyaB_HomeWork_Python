from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")


button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
button.send_keys("SkyPro")


updat_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
updat_button.click()


print(updat_button.text)


driver.quit()
