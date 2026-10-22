class library:
    def __init__(self,):
        self.noBooks=0
        self.book=[]
    def addbooks(self,book):
        self.book.append(book)
        self.noBooks=len(self.book)
    def showinfo(self):
        i=1
        print(f"no of book is {self.noBooks}")
        for book in self.book:
            print(f"{i}. {book}")
            i+=1

l1=library()
l1.addbooks("the lord kingdom")
l1.addbooks("lord attitude")
l1.addbooks("the epic battle")
l1.showinfo()
