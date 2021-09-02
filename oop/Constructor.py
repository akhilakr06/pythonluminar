class Person:
    def __init__(self,name,age):#constructor.....initialize instance variables
        self.name=name
        self.age=age
    def printVal(self):
        print(self.name,self.age)
p=Person("annu",26)
p.printVal()
