# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.XPATH, "//a[text()='JavaScript Alerts']").click()
# sleep(2)
# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# print(driver.find_element(By.CSS_SELECTOR, "#result").text)
# sleep(2)
# driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
# sleep(2)
# alert.dismiss()
# print(driver.find_element(By.ID, "result").text)
# driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
# sleep(2)
# alert.send_keys("I am JS executor")
# sleep(1)
# alert.accept()
# print(driver.find_element(By.CSS_SELECTOR, "#result").text)
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH, "//a[text()='JavaScript Alerts']").click()
sleep(2)
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
print(driver.find_element(By.CSS_SELECTOR, "#result").text)
sleep(2)
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
sleep(2)
alert.dismiss()
print(driver.find_element(By.ID, "result").text)
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
sleep(1)
alert.send_keys("I am a JS executor")
sleep(2)
alert.accept()
print(driver.find_element(By.CSS_SELECTOR, "#result").text)
driver.quit()