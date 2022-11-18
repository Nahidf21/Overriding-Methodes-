class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def __str__(self):
        return 'The Titel of the book is : {} and the Author of the book: {}'.format(self.title,self.author)

class Ebook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self,title,author)
        self.size=size

class PaperBook(Book):
    def __init__(self,title,author, page):
        Book.__init__(self,title,author)
        self.page=page

class library:

    def __init__(self):
        self.books=[]
    
    def addbook(self,name_of_book):
        self.books.append(name_of_book)

    def return_number(self):
        return len(self.books)


Book_info=Book("Love","Nahid")
Book_infoE=Ebook("My_love","Ferdous",62)
Book_infoPaper_boook=PaperBook("Interviwe","Marzia Khan",500)

Dhaka_library= library()
Dhaka_library.addbook("The HIstory of bangladesh")
Dhaka_library.addbook("The libaretion ware of Bangladesh")
Dhaka_library.addbook("Dencity of the populetion in Dhaka")

pri=Dhaka_library.return_number()
print(pri)