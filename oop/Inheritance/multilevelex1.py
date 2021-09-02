class Person:
    def setVal(self,name,id):
        self.name=name
        self.id=id
        print(self.name,id)
class Child(Person):
    def getVal(self,add,mark):
        self.add=add
        self.mark=mark
        print(self.add,self.mark)
class Student(Child):
    def printVal(self,regno,div,percentage):
        self.regno=regno
        self.div=div
        self.percentage=percentage
        print(self.div,self.regno,self.percentage)
stud=Student()
stud.setVal("anu",12)
stud.getVal("abc addrsss",2541)
stud.printVal(902156,"MCA",70)