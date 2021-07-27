from locust import HttpUser, TaskSet, task
from res import requts

class UserTasks(TaskSet,requts):
    # 列出需要测试的任务形式一
    @task
    def login(self):
        url = 'https://www.i-school.net/login/doLogin'
        params = self.reqs()
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        res = self.client.post(url,params,headers=header,verify=False)
        if res.status_code == 200:
            print(params)
        else:
            print("失败")
        print(res.text)


class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    min_wait = 0
    max_wait = 0
if __name__=="__main__":
    import os
    os.system("locust -f yali.py --host=https://www.i-school.net/login/doLogin")