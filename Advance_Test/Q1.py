class Vehicle:
    def __init__(self,colour,model,regnum):
        self.colour=colour
        self.model=model
        self.regnum=regnum
    def printy(self):
        print("Colour:",self.colour)
        print("Register number:",self.regnum)
        print("Model name:",self.model)
class Bus(Vehicle):
    def __init__(self):
        super().__init__(colour,model,regnum)

c=Vehicle("blue","Bus",1234)
c.printy()
