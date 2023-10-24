from q1 import Book

class BookNotAvailable(Exception):
    pass

class InsufficientCopies(Exception):
    pass
    
if __name__=='__main__':
    books=[]
    with open('books.txt','r') as fp:
        for line in fp.readlines():
            line=line.strip('\n')
            details=line.split(',')
            books.append(Book(details[0],details[1],details[2],details[3],details[4]))
    while True:
        try:
            title = input("Enter book to search: ")
            flag=False
            for book in books:
                if book.title.lower()==title.lower():
                    flag=True
                    print(f"\nDETAILS\nAuthor - {book.author}\nTitle - {book.title}\nPrice - {book.price}\nPublisher - {book.publisher}") 
                    try:
                        copies=int(input("\nEnter copies required: "))
                        if copies<=book.stock:
                            print("Total cost: ",copies*book.price,"\n")
                        else:
                            raise InsufficientCopies
                    except InsufficientCopies:
                        print("Insufficient Copies in Stock")
            if flag==False:
                raise BookNotAvailable
        except BookNotAvailable:
            print("Book not avaliable....")