class a:
    def __init__(self):
        self.tt = 1
class b(a):
    def c(self):
        print(self.tt)

b().c()