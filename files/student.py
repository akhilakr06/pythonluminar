class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printv(self):
        print(self.name,self.age)
f=open('stud','r')
for i in f:
    print(i)
    l=i.split(",")
    # print(l)
    name=l[0]
    age=l[1]
    st=Student(name,age)
    # print(st)
    # st.printv()
# s=Student()
# s.printv()