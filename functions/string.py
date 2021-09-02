# string=input("enter a string")
# c=input("enter a character")
# # for i in string:
# if c in string:
#     print("present")
# else:
#     print("not present")

string=input("enter a string")
c=input("enter a character")
flag=0
for i in string:
    for  i in c:
        flag=1
if flag==1:
    print("present")
else:
    print("not present")