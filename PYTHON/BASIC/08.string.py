a = "adiTya !!!"
print(a[1])
for character in a:
    print(character)

print(a.find("i"))
print(a.index("ads")) #index method is same as find(), when value is not found it will f=give error intead of -1.
print(a.replace("i","a"))
print(len(a))
print(a.count("a"))
print(a.capitalize())
print(a.endswith("ya"))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
b="aditya kumar sahu"
print(b.split(" "))
#splits the string at the white space " "
print(len(b))
print(b.center(50,"*"))
print(b.isspace())

