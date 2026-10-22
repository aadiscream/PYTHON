class emp:
    company="Appple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
    @classmethod
    def changeCompany(cls, newcompany):
        cls.company=newcompany
    
e1=emp()
e1.name="Aditya"
e1.show()
print(emp.company)
e1.changeCompany("Google")
e1.show()
print(emp.company)
