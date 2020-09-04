from locators import Locator
import time

class LogoutPage():

    def __init__(self, driver):
        self.driver = driver

        self.profile = Locator.profile
        self.logout = Locator.logout

    def click_profile(self):
        self.driver.find_element_by_xpath(self.profile).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout).click()