class Person:
    def setp(self,name,age):
        self.name=name
        self.age=age
    def printp(self):
        print("Name=",self.name)
        print("Age=",self.age)
class Child(Person):
    def setc(self,regno,div):
        self.regno=regno
        self.div=div
    def printc(self):
        print("Register no:",self.regno)
        print("Division:",self.div)
class Student(Child):
    def sets(self,mark):
        self.mark=mark
        print("Mark=",self.mark)

s=Student()
s.setp("akhila",23)
s.printp()
s.setc(12,"XIIA")
s.printc()
s.sets(96)