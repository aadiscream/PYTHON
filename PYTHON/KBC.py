print("!!!! WELCOME TO THE KOUN BNEGA CROREPATI !!!!")
again=int(input("Press 1 To Start........"))
no=0
no1=0
questions = ("Question 1 : What is the core component of a computer's operating system ? ","Question 2 : Which protocol is used to send emails?","Question 3 : What is the main memory of a computer also known as?","Question 4 : Which programming language is known for its use in web development?","Question 5 : What is the basic unit of a digital image called?","Question 6 : Which type of network covers a large geographic area, such as a city or country?")
options=("1) kernal","2) shell","3) interface","4) protocol","1) FTP","2) HTTP","3) SMTP","4) IMAP","1) SSD","2) HDD","3) RAM","4) ROM","1) JAVA","2) C++","3) PYTHON","4) JAVASCRIPT","1) Pixel","2) Byte","3) Bit","4) Node","1) LAN","2) WAN","3) PAN","4) MAN")
answer=(1,3,3,4,1,2)
reward=(0,1000,10000,"1 Lakh","10 Lakhs","1 Crore", "7 Crores")
def kbc(no,no1):
    print(questions[no])
    for i in range(no1,no1+4):
        print(options[i],"\t")
    ans=int(input("Enter 1/2/3/4 : "))
    if(ans==answer[no]):
        print("!! WOW You Won",reward[no+1],"!!")
    else:
        print("Your Winning amount is :",reward[no])
        return 0
if(again==1):
 while(no<7 ):
    kbc(no,no1)
    no+=1
    no1+=4
 