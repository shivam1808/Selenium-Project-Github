from locators import Locator
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.signin_button = Locator.signin_button
        self.username = Locator.username
        self.password = Locator.password
        self.signin = Locator.signin

    def click_signin_button(self):
        self.driver.find_element_by_link_text(self.signin_button).click()
        time.sleep(3)

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username).clear()
        self.driver.find_element_by_id(self.username).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)
        

    def click_signin(self):
        self.driver.find_element_by_name(self.signin).click()

    