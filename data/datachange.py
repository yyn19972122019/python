# 安装 xlrd 1.2版本 pip install xlrd==1.2.0
import xlrd
def opxlrd(xlsfile=None):
    dalist = []
    book = xlrd.open_workbook('\Test_UIpython\data\data.xls')
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