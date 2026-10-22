def cube(x):
    return x*x*x
l=[1,2,4,6,4,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))
newl=list(map(cube,l))
print(newl)