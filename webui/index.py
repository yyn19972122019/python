from selenium import webdriver

import config_file.config

from selenium.webdriver.common.by import By
from time import sleep
from base import BasePage
from webui.web import LoginPage


class IndexPage(BasePage.BasePage):
    def lists(self,one,two,three):
        self.click((By.CSS_SELECTOR,'.left-menu>ul>li:nth-child(4)'))
        sleep(3)
        self.click((By.CSS_SELECTOR,'.left-menu>ul>li:nth-child(4)>ul>li:nth-child(15)'))
        sleep(3)
        self.click((By.CSS_SELECTOR,'.left-menu>ul>li:nth-child(4)>ul>li:nth-child(15)>ul>li:first-child'))
        sleep(3)
        self.click((By.CSS_SELECTOR, '.wnTitle>a'))
        sleep(3)
        self.input_((By.CLASS_NAME,'checking-name'),one)
        self.input_((By.NAME,'honor-level'),two)
        self.click((By.ID,'chooseDate'))
        sleep(2)
        self.click((By.CSS_SELECTOR, '.laydate-footer-btns>span:nth-child(2)'))
        sleep(1)
        self.click((By.CLASS_NAME, 'u-select'))
        sleep(2)
        self.click((By.CSS_SELECTOR, '.u-select>div:nth-child(3)>div:first-child'))
        sleep(2)
        self.input_((By.NAME, 'honor-unit'), three)
        sleep(2)
        self.click((By.CSS_SELECTOR,'.btn-box>a'))
        sleep(2)
        try:
            self.click((By.CSS_SELECTOR, '.u-dialog-foot>button:last-child'))
        except Exception as fail:
            print(fail)
if __name__ == '__main__':
    driver = webdriver.Chrome()
    users = '02400094'
    pwds = '123456'
    a = LoginPage(driver)
    a.login(users,pwds)
    b = IndexPage(driver)
    b.lists(11,22,33)
