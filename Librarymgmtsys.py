class Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lenddict={}
    def displaybook(self):
        print(f"Books available in library {self.name}--")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Book has been updated, you can use your book")
        else:
            print(f"Book is already being used by {self.lenddict[book]}")
    def addbook(self,book):
        self.booklist.append(book)
        print("Book hase been added to list")
    def returnbook(self,book):
        self.lenddict.pop(book)
if __name__ == '__main__':
    pankajs=Library(['python','Biology','history','cpp'],"Shribooks")
while True:
    print(f"Welcome to {pankajs.name}.Enter your choise")
    print("1. Displaybook")
    print("2. Lendbook")
    print("3. Addbook")
    print("4. Returnbook")
    choise1=int(input())
    if choise1 == 1:
        pankajs.displaybook()
    elif choise1 == 2:
        book=input("Enter the book name you want to lend -")
        user=input("Enter the name -")
        pankajs.lendbook(user,book)
    elif choise1 == 3:
        book=input("Enter the book name you want add - ")
        pankajs.addbook(book)
    elif choise1 == 4:
        book=input("Enter the book name you want to return - ")
        pankajs.returnbook(book)
    else:
        print("Invalid input")

    print("press c to continue or q to quit")
    choise2 = input()
    while(choise2 =="c"and choise2 == "q"):

        if choise2 == "q":
            exit()

        elif choise2 == "c":
            continue




