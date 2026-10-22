def greet(fx):
    def mfx():
        print("hii")
        fx()
        print("bye")
    return mfx

@greet
def gdmorning():
    print("good morning")

# greet(gdmorning)() #but you dont have to write @greet above the gdmorning function
gdmorning()