class person:
    name="aditya"
    roll=17
    age=19
    college="DSPMU"
    def info(self):
        print(f"{self.name} is a {self.age} years old who study in {self.college},\nhis roll no is {self.roll}")

a=person()
a.info()