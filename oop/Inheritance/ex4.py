class Person:
    def set1(self,name):
        self.id=id
        self.name=name
        print(self.name)
class Child(Person):
    def setc(self,id,rollnum):
        self.id=id
        self.rollnum=rollnum
        print(self.rollnum,self.id)
class Parent(Child):
    def setp(self,namec,num):
        self.namec=namec
        self.num=num
        print(self.namec,self.num)
class Student(Child,Person):
    def setstud(self,mark):
        self.mark=mark
        print(self.mark)

stud=Student()
stud.setstud(2541)
stud.setc(21,5844)
p=Person()
p.set1("name")
