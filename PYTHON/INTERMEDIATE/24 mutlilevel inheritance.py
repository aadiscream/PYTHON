class a:
    def __init__(self):
        self.num1=12
class b(a):
    def data(self):
        self.num2=10

class c(b):
    def sub(self):
        self.data()
        print(self.num1-self.num2)
obj=c()
obj.sub()