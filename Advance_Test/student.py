class Student:
    clg="stc"
    def setv(self,name,roll,cource,mark):
        self.name=name
        self.roll=roll
        self.cource=cource
        self.mark=mark
    def printv(self):
        print(self.name,self.roll,self.cource,self.mark,Student.clg)

s=Student()
s.setv("anu",1,"BCA",200)
s.printv()
s.setv("rahul",2,"bba",177)
s.printv()
s.setv("vinod",3,"bba",187)
s.printv()
s.setv("ajay",4,"bca",198)

s.printv()


