
import time,config_file.config,driver.driver as drivers
class denglu(drivers.Diver):
    def login(self,user=None,pwd=None):
        url = config_file.config.configs().redcon('login')
        self.driver.get(url)
        # 清除cookies
        self.driver.delete_all_cookies()
        time.sleep(1)
        self.driver.find_element_by_id("user").send_keys(user)
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys(pwd)
        time.sleep(1)
        self.driver.find_element_by_id("login-btn").click()
        time.sleep(6)
        try:
            right = self.driver.find_element_by_css_selector('.nav>ul>li:first-child>a:first-child').text
            return right
        except Exception:
            faild = self.driver.find_element_by_class_name('form-tip').text
            fs = len(faild)
            if fs:
                return faild
            else:
                le = self.driver.find_element_by_id("login-btn").text
                return le
        finally:
            self.driver.close()

if __name__ == '__main__':
    a = denglu()
    b = a.login('02400094','123457')
    print(b)
