a= input("enter string:")
b=input("search character")
c=0
for i in a:
    if i in b:
        c+=1
print("String count:",str(c))
    # print(a)
    # print(b.count(a))