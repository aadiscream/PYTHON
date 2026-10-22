import threading
from time import sleep
def work(sec):
    print(f"sleeping for {sec} seconds")
    sleep(sec)
#normal code
# work(4)    
# work(2)    
# work(3)    
#uisng multithread
t1=threading.Thread(target=work, args=[4])
t2=threading.Thread(target=work, args=[2])
t3=threading.Thread(target=work, args=[3])  
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()