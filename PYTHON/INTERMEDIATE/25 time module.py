import time
# print(time.time())
#1741423004.677795
def usingwhile():
    i=0
    while(i<50000):
        print(i)
        i+=1
def usingfor():
    for i in range(1,50000):
        print(i)
whilestart=time.time()
usingwhile()
whileEnd=time.time()
forstart=time.time()
usingfor()
forend=time.time()
print(f"while {whileEnd-whilestart:.5f} sec \nfor {forend-forstart:.5f} sec")
time.sleep(4) #sleep for 4 seconds
print("printed after 4 seconds")