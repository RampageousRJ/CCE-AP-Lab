class Book():
    def __init__(self,author,title,price,publisher,stock):
        self.author = author
        self.title = title
        self.price = int(price)
        self.publisher = publisher
        self.stock = int(stock)

    def __del__(self):
        print("Destructor Called")
    
if __name__=='__main__':
    books=[]
    with open('books.txt','r') as fp:
        for line in fp.readlines():
            line=line.strip('\n')
            details=line.split(',')
            books.append(Book(details[0],details[1],details[2],details[3],details[4]))
    title = input("Enter book to search: ")
    flag=False
    for book in books:
        if book.title.lower()==title.lower():
            flag=True
            print(f"\nDETAILS\nAuthor - {book.author}\nTitle - {book.title}\nPrice - {book.price}\nPublisher - {book.publisher}") 
            copies=int(input("\nEnter copies required: "))
            if copies<=book.stock:
                print("Total cost: ",copies*book.price,"\n")
            else:
                print("Required copies not in stock\n")
    if flag==False:
        print("Not available\n")