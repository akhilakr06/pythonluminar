num=int(input("number"))
f=1
if num>0:
    for i in range(1,num+1):
        f=f*i
    print(f)
elif num==0:
    print("factorial of 0 is 1")
else:
    print("enter a postive number!!!")