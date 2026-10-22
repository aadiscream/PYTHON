x = (input("enter number b/w 5 to 9 :"))
if(x=="quit"):
    print("QUIT")
elif(int(x)>9 or int(x)<5):
    raise ValueError("enter number b/w 5 to 9 ")
else :
    print(int(x))