class base:
    def __init__(self):
        self.num1=10
        self.num2=20
class a1(base):
    def increment1(self):
        self.num1+=10
class a2(base):
    def increment(self):
        self.num1+=20 
class add(a1,a2):
    def addition(self):
        self.increment()
        self.increment1()
        print(self.num1+self.num2)
obj=add()
obj.addition()