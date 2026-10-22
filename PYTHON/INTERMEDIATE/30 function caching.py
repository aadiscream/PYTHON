from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5
print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(4))
print("done for 4")
print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(41))
print("done for 41")