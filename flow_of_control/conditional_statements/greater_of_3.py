n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))
if n1>n2 and  n1>n3:
    print("num1 is largest", n1)
elif n2>n1 and n2>n3:
    print("num2 is largest",n2)
elif n1==n2 and n2==n3:
    print("equalss")
else:
    print("num3 is largest",n3)