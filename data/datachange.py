# 安装 xlrd 1.2版本 pip install xlrd==1.2.0
import xlrd,os
def opxlrd(xlsfile=None):
    dalist = []
    # 使用os获取当前文件父目录下的data文件,绝对路径,谁都可以访问到,因为使用别的文件运行时都是以
    # 当前运行文件作为视角运行的所以要一个绝对路径,让谁都可以访问测试文件
    father_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")
    # 判断是否在python目录,如果文件的父目录不含有python，那么判断在python目录下就直接访问就可以
    # 如果python是你的父目录,直接拼接,访问 目的就是访问python下的文件不管以什么文件的视角
    if 'python' not in father_path:
        path = fr"{os.getcwd()}\data\data.xls"
    else:
        path = fr"{father_path}\data\data.xls"
    book = xlrd.open_workbook(path)
    # 获得excel中的表1
    sheet = book.sheet_by_index(0)
    # 获得行数
    nrows = sheet.nrows
    # 行数为循环次数
    for i in range(1,nrows):
        # 获取每一行的数据  i代表行数,0代表列数据
        hope = sheet.cell_value(i,0)
        user = sheet.cell_value(i,1)
        pwd = int(sheet.cell_value(i,2))
        data = {}
        data["user"] = user
        data["pwd"] = pwd
        data["hope"] = hope
        dalist.append(data)
    iter_obj = (i for i in dalist)
    return iter_obj
if __name__ == '__main__':
   a = opxlrd()
   print(list(a))