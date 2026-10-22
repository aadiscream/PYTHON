class emp:
    company_name="google" #class variable
    noOfEMP = 0
    def __init__(self,name):
        self.name=name
        self.raise_amt=0.02 #instance  variable
        emp.noOfEMP +=1
    def show(self):
        print(f"{emp.noOfEMP} name = {self.name}, company = {self.company_name}, raise amount {self.raise_amt}")
# emp.show(adi)
adi=emp("adi")
adi.raise_amt=0.8
adi.show()
rohan=emp("rohan")
rohan.show()
emp.company_name="GOOGLE" # to change class variable