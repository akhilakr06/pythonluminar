# get 5 marks from student and calculate total and average

print("...Student Details...")
name=input("Enter student name:")
mark1=int(input("Enter sub1 mark/50:"))
mark2=int(input("Enter sub2 mark/50:"))
mark3=int(input("Enter sub3 mark/50:"))
mark4=int(input("Enter sub4 mark/50:"))
mark5=int(input("Enter sub4 mark/50:"))
total = mark1+mark2+mark3+mark4+mark5
avg=total/5
print("Name :", name)
print("Marks obtained for 5 subjects.../50")
print("Mark1=",mark1,"Mark2=",mark2,"Mark3=",mark3,"Mark4=",mark4,"Mark5=",mark5)
print("Total ",total)
print("average ",avg)
if avg>90:
    print("A+")
elif 80<=avg<=90:
    print("A")
elif 70<=avg<=80:
    print("B+")
elif 60<=avg<=70:
    print("B")
elif 50<=avg<=60:
    print("C+")
elif 40<=avg<=50:
    print("C")
elif 30<=avg<=40:
    print("D")
else:
    print("failed!!!")