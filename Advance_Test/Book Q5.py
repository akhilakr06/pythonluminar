
class Book():
    def __init__(self):
        self.value = "Reading"
    def show(self):
        print(self.value)
class Child(Book):
    def __init__(self):
        self.value = "Studying"
    def show(self):
        print(self.value)



obj1 = Book()
obj2 = Child()

obj1.show()
obj2.show()