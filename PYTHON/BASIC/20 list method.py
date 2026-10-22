abc=["a","f","v","b"]
num=[1,2,5,3,2]
abc.sort() #sort abc in alphabetic order
num.sort()
num.append(-1) #isko sort nahi krega qki iako sort krne ke baad add kiya jaa rha hai
print(abc)
print(num)
num.sort(reverse=True)
print(num)
abc.insert(2,45)
print(abc)
abc.extend(num)
print(abc)
print(abc+num)