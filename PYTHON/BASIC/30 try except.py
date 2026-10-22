a = input("enter any no  : ")
print("table of",a," is :")
try:
 for i in range(11):
  print(f"{int(a)} X {i} = {int(a)*i}")
# except: #or
except Exception as e:
#  print(e) # used to show error type
 print("sorry for error")
 print("some imp code")