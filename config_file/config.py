import configparser
class configs:
    def __init__(self):
        self.cf = configparser.ConfigParser()
    def redcon(self,name:str)->list:
        try:
            filename = self.cf.read("\Test_UIpython\config_file\config.ini")
            print(filename)
            value = self.cf.get(name,"url")
            return value
        except Exception as res:
            print(res)

if __name__ == '__main__':
    a = configs()
    b = a.redcon('login')
    print(b)