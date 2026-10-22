def generator():
    for i in range (5):
        yield i

gen = generator()
print(next(gen))
print(next(gen))
# while True:
#     print(next(gen))
for j in gen:
    print(j)