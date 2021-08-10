# import  datetime
# # class a:
# #     def __init__(self,year,month,day):
# #         self.year = year
# #         self.month = month
# #         self.day = day
# #     @property
# #     def pro(self):
# #         print(f'{self.year}年,{self.month}月,{self.day}日')
# #     @classmethod
# #     def ptt(cls,data):
# #         year,month,day = map(int,data.split('-'))
# #         date1 = cls(year,month,day)
# #         return date1
#
#
# # 声明一个辅助函数(添加辅助功能,比如记录当前的系统时间)
# # 装饰器其实就是语法糖,简化了闭包的调用的繁琐,而且把函数独立起来,互不影响
# # 比如你可能会修改主函数的内容,但是不会影响到辅助函数,辅助函数同理
# def times(fun):
#    # 声明一个wapper增加一些辅助功能,获取当前时间
#    # *args的意思是不知道你要传多少个参数,但是我都接收,接收的是主函数的参数
#    def wapper(*args):
#       # 辅助函数功能
#       print(datetime.datetime.now())
#       # 接收并调用主函数并传递参数
#       return fun(*args)
#    return wapper
# # 添加装饰器,在装饰器下添加主函数
# # 简化了闭包的调用方式 闭包的方式为 c = times(pt),直接调用主函数对于使用者来说更符合逻辑
# @times
# # 声明一个主函数(打印输出内容)
# def pt(s):
#    return s
# if __name__ == '__main__':
#    # 辅助函数的包装过程,无须调用隐藏掉了已经,仅仅调用主函数就好了
#    c = pt("d")
#    print(c)
# a = 1
# def b():
#     global a
#     a = 2
#     print(a)
# b()
# print(a)