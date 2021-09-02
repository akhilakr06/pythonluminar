class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printVal(self):
        print("name",self.name)
        print("age",self.age)
class Employee(Person):
    def __init__(self,job,sal,name,age):
        super().__init__(name,age)
        self.job=job
        self.sal=sal
    def printy(self):
        print(self.job)
        print(self.sal)
emp=Employee("devu",5000,"nnu",54)
emp.printVal()
emp.printy()

        #  car claasss
        #  model reg no colour