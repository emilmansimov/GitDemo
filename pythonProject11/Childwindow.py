# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common import window
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
#
# service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.maximize_window()
# driver.get("https://trade.thinkorswim.com")
# sleep(1)
# driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
# window = driver.window_handles
# driver.switch_to.window(window[1])
# sleep(2)
# driver.close()
# driver.switch_to.window(window[0])
# print(driver.current_url)
# sleep(1)
# driver.find_element(By.NAME, "su_username").send_keys("blah")
# sleep(2)
# driver.switch_to.window(window[0])
# print(driver.current_url)
# driver.close()
# driver.quit()
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
driver.maximize_window()
driver.get("https://trade.thinkorswim.com")
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
sleep(2)
window = driver.window_handles
driver.switch_to.window(window[1])
sleep(2)
driver.close()
driver.switch_to.window(window[0])
driver.find_element(By.NAME, "su_username").send_keys("Emanmanem251")
print(driver.current_url)
sleep(1)

