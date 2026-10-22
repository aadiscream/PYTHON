class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=person("aditya",19)
print(p.__dict__)
#__dict__ is a dictionary representation of an object's attributes
print(help(person))
#help() is used to get help documentation for an object, includeing a description of its attributes and methods