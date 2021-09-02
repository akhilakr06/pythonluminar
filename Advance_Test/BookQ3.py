class Book:
    def __init__(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printv(self):
        print("Library Name=",self.library_name)
        print("Book name:",self.book_name)
        print("Author:",self.author)
        print("Pages:",self.pages)
b=Book("ABC Library","Python Fundeamentals","AK Shivram",120)
b.printv()


