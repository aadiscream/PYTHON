with open('ademofile.txt','r') as f:
    #move to the 4 bytes of the file
    f.seek(4)
    #tell() locate the position
    print(f.tell())
    #read the next 6 bytes
    data=f.read(6)
    print(data)