class BasePage:
    # 获得drver对象
    def __init__(self,driver):
        self.driver= driver
    # 访问url
    def visit(self):
        self.driver.get(self.url)
    # 元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)
    # 元素的输入行为
    def input_(self,loc,txt):
        self.locator(loc).send_keys(txt)
    # 元素点击行为
    def click(self,loc):
        self.locator(loc).click()
    # 获取元素文本
    def text(self,loc):
       return self.locator(loc).text