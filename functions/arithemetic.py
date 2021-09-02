def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return(x*y)
def div(x,y):
    return x/y


print("...Select Operator...")
print("1.Add")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

while True:


    ch = int(input("enter your choice(1/2/3/4/5):"))
    num1=int(input("enter number 1:"))
    num2=int(input("enter number 2:"))
    if ch==1:
        print(add(num1,num2))
    elif ch==2:
        print(sub(num1,num2))
    elif ch==3:
        print(mul(num1,num2))
    elif ch==4:
        print(div(num1,num2))
    else :
        print("Invalid choice...!!!!")
        exit()