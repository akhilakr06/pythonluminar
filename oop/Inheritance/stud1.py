class Student:
    clg="stc"
    def __init__(self,name,roll,dept):
        self.name=name
        self.roll=roll
        self.dept=dept
        # self.clg=clg
    def printv(self):
        print(self.name,self.roll,self.dept,Student.clg)
    def __str__(self):
        return self.name+self.dept+str(self.roll)
s=Student("anu",12,"Maths")
s.printv()
print(s)