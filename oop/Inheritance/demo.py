class Person:
    def walk(self):
        print("walking")
    def read(self):
        print("Reading")
class Student(Person):
    def exam(self):
        print("student attend exam")

p=Person()
p.walk()
p.read()
s=Student()
s.exam()
s.walk()
s.read()