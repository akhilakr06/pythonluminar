class Employee:
    company_name="ucc"
    def __init__(self,name,id,sal):

        self.name=name
        self.id=id
        self.sal=sal
       # self.company_name=company_name
    def printValue(self):
        print(self.name,self.id,self.sal,Employee.company_name)
emp=Employee("ammu",54,25000)

emp.printValue()
emp1=Employee("anju",47,12000)

emp1.printValue()
