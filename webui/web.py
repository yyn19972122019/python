from selenium import webdriver

import config_file.config

from selenium.webdriver.common.by import By
from time import sleep
from base import BasePage

class LoginPage(BasePage.BasePage):
    url = config_file.config.configs().redcon('login')
    user = (By.ID,"user")
    pwd = (By.ID,"password")
    button = (By.ID,"login-btn")
    def login(self,users=None,pwds=None):
        self.visit()
        # 清除cookies
        self.driver.delete_all_cookies()
        sleep(1)
        self.input_(self.user,users)
        sleep(1)
        self.input_(self.pwd,pwds)
        sleep(1)
        self.click(self.button)
        sleep(6)
if __name__ == '__main__':
    driver = webdriver.Chrome()
    users = '02400094'
    pwds = '123456'
    a = LoginPage(driver)
    a.login(users,pwds)
