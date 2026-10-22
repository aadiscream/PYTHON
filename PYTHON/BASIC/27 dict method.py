dict={1:"aditya",1:"aitya",
      2:"adi",
      3:"amit"}
# print(dict)
dict.update({4:"sumit"})
dict.update({2:"kunal"})
# print(dict)
dict2={6:"himanshu",
       7:"sonal"}
dict.update(dict2)
# print(dict)
# dict.clear() #it clears all the data of dict
dict.pop(1)
print(dict)
dict.popitem()
print(dict)
# del dict
del dict[3]
print(dict)