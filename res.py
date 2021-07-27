import  requests,test_aes
class requts:
    def reqs(self):
        url = 'https://www.i-school.net/login/preLogin'
        Sess = requests.Session()
        res = Sess.get(url).json()["data"]["iv"]
        url = 'https://www.i-school.net/login/doLogin'
        tt = test_aes.Encrypt("31bdd416fcea34d1", res)
        pwd = tt.aes_encrypt("970208")
        params = {
            "account": 18117924300,
            "password": pwd,
            "iv": res,
            "confuse": "aes-128-cbc",
            "dosubmit": "true",
            "referer": "",
            "role": 1,
            "rememberMe": 0
        }
        # res = Sess.post(url,params)
        return  params
if __name__ == '__main__':
    ddd = requts().reqs()
    print(ddd)