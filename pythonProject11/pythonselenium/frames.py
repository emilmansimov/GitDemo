from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/iframe")
sleep(2)
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#mce_0_ifr"))
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
sleep(1)
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("Hi im your first iframe code")
driver.switch_to.default_content()
text_conformation = driver.find_element(By.XPATH, "//div/h3").text
print(text_conformation)