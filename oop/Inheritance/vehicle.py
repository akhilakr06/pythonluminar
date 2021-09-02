class Vehicle:
    def __init__(self,colour,model,regnum):
        self.colour=colour
        self.model=model
        self.regnum=regnum
    def printy(self):
        print(self.colour)
        print(self.regnum)
        print(self.model)
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__(colour,model,regnum)
    def __str__(self):
        return self.model+self.colour
c=Vehicle("yello","BMW",1234)
c.printy()
print(c)