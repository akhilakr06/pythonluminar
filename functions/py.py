str=input("enter string:")
b=""
for i in str:
    if i not in b:
        b=b+i
    else:
        print(i)
        break