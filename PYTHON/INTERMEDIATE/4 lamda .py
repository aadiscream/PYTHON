# def double(x):
#     return x*2
# now using lamda for same program
double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2
print(double(5))
print(cube(5))
print(avg(5,3))
def appl(fx,value):
    return 6+fx(value)
# print(appl(cube,3))
#OR
print(appl(lambda x: x*x*x,3))