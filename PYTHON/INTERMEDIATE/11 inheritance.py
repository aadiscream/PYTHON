class baseclass:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"{self.name}'s id no is {self.id}")
class derivedclass(baseclass):
    def goodboy(self):
        print(f'{self.name} id good boy')

# e = baseclasss("aditya",17)
e = derivedclass("aditya",17)
e.show()
e.goodboy()