class student:
    def __init__(self,name):
        self.__name=name

a=student("adi")
# print(a.__name) #it is private (__)
print(a._student__name)