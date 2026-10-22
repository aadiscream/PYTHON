f=open('ademofile.txt','r')
while True:
  line=f.readline()
  print(line)
  if not line:
    print("end")
    break