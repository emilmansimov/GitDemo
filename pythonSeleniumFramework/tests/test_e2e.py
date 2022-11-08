from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.TradePage import TradePage
from testLoginData.TestLoginData import TestData
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage

class TestE2E(BaseClass):
    def test_end_to_end(self, data_load):
        login = LoginPage(self.driver)
        login.get_username().send_keys(data_load["username"])
        login.get_password().send_keys(data_load["password"])
        self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
        self.driver.find_element(By.ID, "accept").click()
        # login.get_checkbox().click()
        # login.get_login_button().click()
        trade = TradePage(self.driver)
        trade.get_trade_button().click()
        trade.get_symbol().send_keys("TW")
        trade.get_symbol_lookup().click()
        trade.get_side().click()
        trade.get_quantity().click()
        for i in range(3):
            trade.get_quantity_input().send_keys(Keys.BACK_SPACE)
        trade.get_quantity_input().send_keys(15)
        sleep(1)
        trade.get_review_order().click()
        trade.get_send_order().click()
        trade.get_notification().click()
        trade.get_order_confirmation()
        sleep(2)
        trade.get_logout_button().click()


    @pytest.fixture(params=TestData.test_data)
                           # {"username": "Emanom222", "password": "Manumemon231"}])
    def data_load(self, request):
        return request.param

