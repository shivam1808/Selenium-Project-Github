from locators import Locator
import time

class NewRepo():

    def __init__(self, driver):
        self.driver = driver

        self.new_repo = Locator.new_repo
        self.repo_name = Locator.repo_name
        self.readMe = Locator.readMe
        self.create_repo = Locator.create_repo

    def new_button(self):
        self.driver.find_element_by_link_text(self.new_repo).click()

    def enter_repo_name(self, repository):
        self.driver.find_element_by_id(self.repo_name).send_keys(repository)
        time.sleep(2)

    def tick_readMe(self):
        self.driver.find_element_by_xpath(self.readMe).click()

    def create_repository(self):
        self.driver.find_element_by_xpath(self.create_repo).click()