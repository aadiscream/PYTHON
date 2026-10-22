with open('ademofile2.txt','w') as f:
    f.write("hey aditya how are you")
    f.truncate(10)

with open('ademofile2.txt','r') as f:
    print(f.read())