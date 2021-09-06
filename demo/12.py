class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printv(self):
        print("iam ",self.name,"iam",self.age,"years old")
class Dog(Animal):
    def set(self,sound):
        self.sound=sound
        print("Dog is",self.sound)

d=Dog("Dog_Buddy",6)
d.printv()
d.set("Barking")
