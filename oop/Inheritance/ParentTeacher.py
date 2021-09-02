class Parent:
    def __init__(self,name,address):
        self.name=name
        # self.id=id
        self.address=address
    def printv(self):
        print("name",self.name)
        # print(self.id)
        print("addr",self.address)
class Teacher(Parent):
    def __init__(self,id,dept,name,address):
        super().__init__(name,address)
        self.id=id
        self.dept=dept
    def printVa(self):
        print("id",self.id,"dept",self.dept)
    def __str__(self):
       return  self.name + " "+ str(self.id)

t=Teacher("annu",12,"KBSHA","ass")
t.printv()
t.printVa()
print(t)
# constructor
# inheritance
# common=name,id()