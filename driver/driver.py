
from selenium import webdriver
class Diver():
    def __init__(self):
        self.driver = webdriver.Chrome()

if __name__ == '__main__':
    a = Diver()
    a.driver.get('https://www.baidu.com/')