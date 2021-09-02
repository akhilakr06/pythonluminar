
stack=[]
n=int(input("enter the size of stack"))
for i in range(n):
    ele=int(input("enter the element in stack:"))
    stack.append(ele)
print(stack)

def push():
    push_ele=int(input("enter elemeny to add"))
    stack.append(push_ele)
    print("stack elemet after push operation")
    print(stack)
def pop():
    stack.pop()
    print("stack elemet after pop operation")
    print(stack)
def exit():
    exit()
while True:


    ch = int(input("enter your choice(1/2/3):"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        exit()
    else:
        print("invalid choice")



print("stack operations")
print("push")
print("pop")
print("exit")

