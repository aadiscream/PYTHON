x=5 #this is global variable
def local():
    x=10 #this is local variable
    print(f"local variable = {x}")
local()
print(f"global variable = {x}") #local variable cant change the value of global variable