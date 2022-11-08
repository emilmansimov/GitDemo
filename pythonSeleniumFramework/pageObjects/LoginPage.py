from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
    username = (By.XPATH, "//input[@type='text']")
    password = (By.ID, "password1")


    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_checkbox(self):
        return self.driver.find_element(*LoginPage.checkbox)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_logout_button(self):
        return self.driver.find_element(*LoginPage.logout_butto)

# # login.get_checkbox().click()
  #       # login.get_login_button().click()
  #       self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
  #       self.driver.find_element(By.ID, "accept").click()