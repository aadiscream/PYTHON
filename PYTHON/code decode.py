import random
#print(random.randit(5,10)) will give random no including 5,10
#print(random.randrange(5,10)) will give random no not including 5,10
#l=["hi","hello,"hero"]
# print(random.choice(l)) will give random item
rand=["ab@","@3#","afg","!u8","90-","1w+","b34","1we","$r^","[e1","<2d","-sdf","wef","btr","jka","bgr","23f","fd7"]
do=int(input("1 for code \n2 for decode\n"))
string=input("enter any words : ")
word=string.split(" ")
newWord=[]
if(do==1):
    for x in word:
        if len(x)>=3:
            newWord.append(random.choice(rand)+x[1:]+x[0]+random.choice(rand))
        else:
            newWord.append(x[::-1])
    print(" ".join(newWord))
else:
    for x in word:
        if len(x)>=3:
            newWord.append(x[-4]+x[3:-4])
        else:
            newWord.append(x[::-1])
    print(" ".join(newWord))