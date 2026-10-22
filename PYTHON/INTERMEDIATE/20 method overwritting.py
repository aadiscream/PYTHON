class rec:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y

class cicle(rec):
    def __init__(self, x):
        self.x=x
    def area(self):
        return 3.14*self.x

a=rec(5,6)
print(a.area())
b=cicle(7)
print(b.area())
