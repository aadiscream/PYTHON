dict = {"name":"aditya",
        "class":"bca",
        "age":19,
        17:"roll no"}
# print(dict[10+7])
print(dict.keys())
print(dict.values())
print(dict.items())
# print(dict["name"])
# for key in dict.keys():
#     print(dict[key])
for key in dict.keys():
    print(f"{key} is {dict[key]}")