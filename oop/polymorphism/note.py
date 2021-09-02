# overriding
#same method name and same no of arguments
# overloading
# same methods  name diff no of parameters
# two types

#overloading is not support in python
#eg:=>
class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(self.num2)
        print(self.num3)
s=Student()
s.show(3)


