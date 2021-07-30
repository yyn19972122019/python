
import pytest,webui.web as web,data.datachange as data
import allure
@allure.feature("编辑页面")
class TestLogin:
    # 无法使用--init--，因为pytest你不能去修改pytest类的构造属性
    # def __init__(self):
    #     self.login = webui.web.denglu().login()
    #     self.data = list(data.opxlrd())
    # 登录成功
    @allure.title("登录成功")
    def test_01(self):
        datas = list(data.opxlrd())
        user, pwd, hope = datas[0].values()
        res = web.denglu().login(user,pwd)
        try:
            assert res == hope
        except AssertionError as faild:
            print('与预期结果不一致'+ faild)
    @allure.title("账户或密码错误")
    def test_02(self):
        datas = list(data.opxlrd())
        user, pwd, hope = datas[1].values()
        res = web.denglu().login(user,pwd)
        try:
            assert res == hope
        except AssertionError as faild:
            print('与预期结果不一致'+ faild)
    @allure.title("账号或密码长度不够")
    def test_03(self):
        datas = list(data.opxlrd())
        user, pwd, hope = datas[2].values()
        res = web.denglu().login(int(user),pwd)
        try:
            assert res == hope
        except AssertionError as faild:
            print('与预期结果不一致'+ faild)
if __name__ == '__main__':
    pytest.main(['-vs'])
