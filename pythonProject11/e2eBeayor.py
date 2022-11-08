# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
#
# service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("http://shopping.beeyor.com/shop")
# sleep(2)
# list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
# for item in list_of_items:
#     item.click()
#     if item == driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[2]"):
#         break
# sleep(2)
# actions = ActionChains(driver)
# actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class='cart-contents']")).perform()
# sleep(2)
# actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class='button wc-forward']")).click().perform()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "input[name='coupon_code']").send_keys("Tojtech Automation")
# sleep(2)
# driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()
#
#
# wait = WebDriverWait(driver, 5)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
# print(driver.find_element(By.XPATH, "//div[@role='alert']").text)
#-------------------------------------------------------------------------------------------------------------
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://shopping.beeyor.com/shop")
sleep(2)
list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
for item in list_of_items:
    item.click()
    if item == driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[2]"):
        break
sleep(2)
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class='cart-contents']")).perform()
sleep(2)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class='button wc-forward']")).click().perform()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[id='coupon_code']").send_keys("Tojtech Automation")
sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[value='Apply coupon']").click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
print(driver.find_element(By.XPATH, "//div[@role='alert']").text)



