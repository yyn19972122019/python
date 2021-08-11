import configparser
import os
class configs:
    def __init__(self):
        self.cf = configparser.ConfigParser()
    def redcon(self,name:str)->list:
        try:
            father_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")
            if 'python' not in father_path:
                path = fr"{os.getcwd()}\config_file\config.ini"
            else:
                path = fr"{father_path}\config_file\config.ini"
            filename = self.cf.read(path)
            # print(filename)
            value = self.cf.get(name,"url")
            return value
        except Exception as res:
            print(res)

if __name__ == '__main__':
    father_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")
    if 'python' in father_path:
        path = fr"{os.getcwd()}\config_file\config.ini"
        print(os.getcwd())
    # a = configs()
    # b = a.redcon('login')
    # print(b)