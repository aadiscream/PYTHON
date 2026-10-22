from functools import reduce
l=[1,2,3]
sum=reduce(lambda x,y:x+y ,l)
print(sum)