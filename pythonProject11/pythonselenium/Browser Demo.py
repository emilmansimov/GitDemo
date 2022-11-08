from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\Users\\Emil\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://trade.thinkorswim.com/")
print(driver.title)
print(driver.current_url)
sleep(2)
driver.get("https://www.apple.com/")
sleep(2)
driver.back()   # back, forward, and refresh are three different methods for a certain type of operation
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.close()  # closes only one tab, the tab that your execution stopped at \,
# so when working with many tabs use driver.quit


