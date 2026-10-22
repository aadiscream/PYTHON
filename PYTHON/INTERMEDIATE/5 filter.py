l=[2,3,4,5,6,7]
def ab(x):
 return x%2==0
newl=list(filter(ab,l))
# newl=list(filter(lambda x: x%2==0,l))
print(newl)