class Person:
    def set(self,id,name):
        self.id=id
        self.name=name
        print(self.id,self.name)
class Child:
    def get(self,school,div):
        self.school=school
        self.div=div
        print(self.school, self.div)
class Student(Person,Child):
    def printv(self,roll,mark):
        self.roll=roll
        self.mark=mark
        print(self.roll, self.mark)

st=Student()
st.set(12,"ammu")
st.get("ucc","B")
st.printv(12,250)


