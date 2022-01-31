class Bookstore:

    NoOfBooks=0

    def __init__(self,a,b):
        self.Name=a
        self.Author=b
        Bookstore.NoOfBooks=Bookstore.NoOfBooks+1

    def Display(self):
        print(self.Name,"by",self.Author,"No of books: ",Bookstore.NoOfBooks)

def main():
    Obj1=Bookstore("Linux System Programming","Robert Love")
    Obj1.Display()

    Obj2=Bookstore("C Programming","Dennis Ritchie")
    Obj2.Display()

if __name__=="__main__":
    main()
