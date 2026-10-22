letter="""DEAR! <your name>
You are selected!! 
<date>"""
name=input("your name : ")
date=input("enter date : ")
letter = (letter.replace("<your name>",name))
letter = (letter.replace("<date>",date))
print(letter)