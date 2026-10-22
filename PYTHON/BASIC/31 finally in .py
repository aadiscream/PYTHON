def func():  
 try:
  l= [10,23,45,5]
  x=int(input("enter any no :"))
  print(l[x])
  return 1
 except:
    print("some error")
    return 0
 finally: #func return kre v to v finally execute krta hai
    print("always executed")

x=func()
print(x)