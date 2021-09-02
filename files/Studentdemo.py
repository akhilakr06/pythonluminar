class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printV(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.mark)
f=open('stud12','r')
for i in f:
    print(i)
    data=i.split(",")
    # print(l)

    name=data[0]
    rollno =data[1]
    course=data[2]
    mark=data[3]

    st=Student(name,rollno,course,mark)

    # st.printV()
