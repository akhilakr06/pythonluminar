class Student:
    school_name="ucc"
    def setValue(self,roll_id,name,division_class):
        self.roll_id=roll_id
        self.name=name
        # self.school_name=school_name
        self.division_class=division_class
    def printValue(self):
        # print(self.roll_id,self.name,self.school_name,self.division_class)
        print("ID:", self.roll_id)
        print("Name:",self.name)
        print("School Name:",Student.school_name)
        print("Class Name0:",self.division_class)

s=Student()
s.setValue(21,"anjaley","degree")
s.printValue()
s1=Student()
s1.setValue(22,"ammu","mca")
s1.printValue()

#static variable......class name is used to invoke
#instance variable....self vach call cheyyane attribute inside class and methods(relate to methods)