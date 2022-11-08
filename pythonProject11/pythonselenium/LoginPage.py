from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# //label[@for='rememberuserid']
driver.get("https://trade.thinkorswim.com/")
sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Emanmanem251")


# ID, NAME, CLASS_NAME, LINK_TEXT, TAG_NAME, PARIAL_LINK_TEXT
#
# XPATH - //tag_name[@attribute_name='value'] -> //input[@type='text']
# CSS - tag_name[attribute_name='value'] -> input[type='text']

sleep(3)
driver.find_element(By.ID, "password1").send_keys("Manememan251")
sleep(2)
driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
sleep(2)
driver.find_element(By.CLASS_NAME, "accept").click()
sleep(4)
driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("TW")
driver.close()
# CSS Selector syntax - input[id='navigation-symbol-search']
# Xpath locators syntax - //label[@for='rememberuserid']
# import BY as BY
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://trade.thinkorswim.com//")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("Emanmanem251")
sleep(3)
driver.find_element(By.ID, "password1").send_keys("Manememan251")
sleep(2)
driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
driver.find_element(By.CLASS_NAME, "accept").click()
sleep(4)
driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("TW")
sleep(2)
driver.find_element(By.XPATH, "//span[text()='TRADEWEB MARKETS INC COM CL A']").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@direction='buy']").click()
driver.find_element(By.XPATH, "//input[@type='number']").click()
sleep(3)

for quantity in range(3):
    driver.find_element(By.XPATH, "//input[@type='number']").send_keys(Keys.BACK_SPACE)

driver.find_element(By.XPATH, "//input[@type='number']").send_keys(15)
sleep(1)
driver.find_element(By.CSS_SELECTOR, "#review-order-button").click()
driver.find_element(By.CSS_SELECTOR, "#send-order-button").click()
driver.find_element(By.XPATH, "//div[text()= 'Notifications']").click()
original_confirmation = []
original_message = [driver.find_element(By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]")]
sleep(3)
print(original_message)

for records in original_message:
    original_confirmation.append(records)
print(original_confirmation)
assert original_message == original_confirmation
# message = "10/10/2022, 10:29 PM EDIT BUY +15 T"
# driver.find_element(By.CSS_SELECTOR, "span[class='menu-button-content']").click()
sleep(4)
driver.close()


