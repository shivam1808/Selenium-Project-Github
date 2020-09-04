from selenium import webdriver
import time
import unittest
import HtmlTestRunner

from loginPage import LoginPage
from newRepo import NewRepo
from logoutPage import LogoutPage

class GitHubTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:\\Software\\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login(self):
        self.driver.get("https://github.com/")

        # self.driver.find_element_by_link_text("").click()
        

        github = LoginPage(self.driver)
        github.click_signin_button()
        github.enter_username("shivam1808")
        github.enter_password("Shivam18@")
        github.click_signin()

        # self.driver.find_element_by_id("login_field").send_keys("shivam1808")
        # self.driver.find_element_by_id("password").send_keys("Shivam18@")
        # self.driver.find_element_by_name("commit").click()

    def test_02_new_repo(self):

        github = NewRepo(self.driver)

        github.new_button()
        github.enter_repo_name("Selenium Work")
        github.tick_readMe()
        github.create_repository()
        # self.driver.find_element_by_link_text("New").click()
        # self.driver.find_element_by_id("repository_name").send_keys("Selenium_Project")
        # time.sleep(2)

        # self.driver.find_element_by_xpath("//body/div/main[@id='js-pjax-container']/div/form[@id='new_repository']/div/div/div[1]/label[1]").click()
        # self.driver.find_element_by_xpath("//button[contains(text(),'Create repository')]").click()

    def test_03_logout(self):

        github = LogoutPage(self.driver)

        github.click_profile()
        github.click_logout()
        # self.driver.find_element_by_xpath("//details[@class='details-overlay details-reset js-feature-preview-indicator-container']//summary[@class='Header-link']").click()
        # self.driver.find_element_by_xpath("//button[@class='dropdown-item dropdown-signout']").click()

    @classmethod
    def tearDownClass(cls): 
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':  
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/shiva/Desktop/Selenium Project GitHub/Report'))