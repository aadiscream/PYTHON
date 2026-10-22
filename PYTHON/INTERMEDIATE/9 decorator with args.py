def greet(fx):
    def mfx(*args, **kwargs):
        print("hello")
        fx(*args,**kwargs)
        print("bye")
    return mfx
@greet
def add(a,b):
    print(a+b)
add(1,2)