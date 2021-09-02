#2,3,5,7,11

number= int(input("enter number"))
flag=0
if number>1:
    for i in range(2,number):
        if number%2==0:
            break
    else:
        flag=1
if flag==1:
    print("prime number")
else:
    print("not prime")
