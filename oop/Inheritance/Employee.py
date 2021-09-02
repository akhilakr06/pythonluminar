class Person:
    def set(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
class Employee(Person):
    def print(self,id,sal,dept):
        self.id=id
        self.sal=sal
        self.dept=dept

        print(self.name)
        print(self.age)
        print(self.address)
        print(self.id)
        print(self.sal)
        print(self.dept)

e=Employee()
e.set("ammu",25,"abc")
e.print(12,25000,"finance")
