class data1:
    def __init__(self):
        self.num1=34
class data2:
    def data(self):
        self.num2=4
class add(data1,data2):
    def addition(self):
        print(self.num1+self.num2)
obj=add()
obj.data()
obj.addition()