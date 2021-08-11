
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.BasePage import BasePage
from data import datachange
from webui.index import IndexPage
from webui.web import LoginPage
@allure.feature("编辑页面")
class TestLogin:
    # 运行初始化
    def setup_class(cls)->None:
        cls.drvier = webdriver.Chrome()
        cls.login = LoginPage(cls.drvier)
        cls.index = IndexPage(cls.drvier)
        cls.Base = BasePage(cls.drvier)
        # cls.data = list(datachange.opxlrd())
    def teardown_class(cls)->None:
        sleep(3)
        cls.drvier.quit()
    @allure.title("账户或密码错误")
    def test_01(self):
        user, pwd, hope = list(datachange.opxlrd())[1].values()
        self.login.login(user,pwd)
        text = (By.CLASS_NAME,"form-tip")
        res = self.Base.text(text)
        try:
            assert res == hope
        except AssertionError as faild:
            print('与预期结果不一致'+ faild)

    # @allure.title("账号或密码长度不够")
    # def test_02(self):
    #     user, pwd, hope = self.data[2].values()
    #     self.login.login(user, pwd)
    #     text = (By.ID, "login-btn")
    #     res = self.Base.text(text)
    #     try:
    #         assert res == hope
    #     except AssertionError as faild:
    #         print('与预期结果不一致' + faild)
    # @allure.title("登录成功")
    # def test_03(self):
    #     user, pwd, hope = self.data[0].values()
    #     self.login.login(user, pwd)
    #     text = (By.CSS_SELECTOR, ".nav>ul>li:first-child>a:first-child")
    #     res = self.Base.text(text)
    #     try:
    #         assert res == hope
    #     except AssertionError as faild:
    #         print('与预期结果不一致' + faild)
    # @allure.title("新增教师荣誉成功")
    # def test_04(self):
    #     try:
    #         self.index.lists(11, 22, 33)
    #         sleep(3)
    #         res = self.Base.text((By.CSS_SELECTOR,'.wntable>tbody>.wntd>td:nth-child(2)'))
    #         assert len(res) > 0
    #     except AssertionError as fail:
    #         print("有错误"+fail)
    # @allure.title("新增荣誉-荣誉名称信息错误")
    # @pytest.mark.parametrize('option',
    #                          [{"one":'',"two":22,"three":33,"code":"!未设置荣誉名称"},
    #                          {"one":'   ',"two":22,"three":33,"code":"!未设置荣誉名称"},
    #                           ])
    # def test_05(self,option):
    #         self.index.lists(option["one"],option["two"],option["three"])
    #         res = self.Base.text((By.CSS_SELECTOR,'.row-item>span:nth-child(4)'))
    #         assert res == option["code"]
    # @allure.title("新增荣誉-荣誉等级错误")
    # @pytest.mark.parametrize('option',[{"one": 11,"two":'',"three": 33,"code":"!未输入荣誉等级"}])
    # def test_06(self, option):
    #         self.index.lists(option["one"], option["two"], option["three"])
    #         res = self.Base.text((By.CSS_SELECTOR,'.edit-box>div:nth-child(2)>span:last-child'))
    #         assert res == option["code"]
if __name__ == '__main__':
    pytest.main(['-vs'])