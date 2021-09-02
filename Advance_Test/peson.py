class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
    def __str__(self):
        return (self.name+str(self.age))
obj=Person("anu ",25)
print(obj)