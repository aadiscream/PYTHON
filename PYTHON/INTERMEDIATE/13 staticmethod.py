class math:
    def __init__(self,num):
        self.num= num
    def addtonum(self,n):
        self.num +=n
    @staticmethod #this is used so that we can add any function that work without any self, 
    #behave as function without the class
    def add(a,b):
        return a+b

a=math(10)
print(a.num)
a.addtonum(5)
print(a.num)
print(a.add(7,5))
print(math.add(3,5))