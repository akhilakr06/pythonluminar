class Person:
    def setValue(self,name,age):
        self.name=name
        self.age=age
    def printValue(self):
        print("Name",self.name)
        print("Age",self.age)

p=Person()
p.setValue('akhila',12)
p.printValue()
