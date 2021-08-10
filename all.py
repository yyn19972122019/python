import pytest
import  os
if __name__ == '__main__':
    pytest.main(['-s','./Testcase/test_one.py','--alluredir','./allure-results'])
#     生成测试报告
    os.system('allure generate ./allure-results -o ./reports')
