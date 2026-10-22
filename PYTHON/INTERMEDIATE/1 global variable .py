x=10
#global variable using global keyword
print(f"global x = {x}")
def variable():
 global x
 x=20
 print(f"global x = {x}")
variable()
print(f"global x = {x}")
