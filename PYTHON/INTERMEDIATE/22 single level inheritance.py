class data:
    def __init__(self):
        self.num1 = int(input("enter any no: "))
        self.num2 = int(input("enter any no: "))

class add(data):
    def addition(self):
        return (self.num1 + self.num2)

b = add()
print(b.addition())