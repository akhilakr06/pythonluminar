class Teacher:
    def __init__(self,tname,tsubject,dept,id,clg_name):
        self.tname=tname
        self.tsubject=tsubject
        self.dept=dept
        self.id=id
        self.clg_name=clg_name
    def display(self):
        print(self.tname,self.tsubject,self.dept,self.clg_name,self.id)
t=Teacher("akhila","english","english","ucc",123)
t.display()
