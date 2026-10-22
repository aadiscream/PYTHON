class parent:
    def parent_method(self):
        print("i am parent")

class baby(parent):
    def baby_method(self):
        print("i am baby")
        super().parent_method()
    def parent_method(self):
        print("i am parent2")
parent_obj=parent()
parent_obj.parent_method()
baby_obj=baby()
baby_obj.parent_method()
baby_obj.baby_method()
#agr baby class ke paas parent method nhi hoga to wo parent class ka parent method run karega 