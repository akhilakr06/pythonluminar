r=int(input("enter initial range"))
# c=int(input("enter final range"))
# x=0
for i in range(1,r+1):
    # x=x+1
    for j in range(1,i+1):
        print("1",end=" ")
    print()
for i in range(r,1,-1):
    for j in range(1,i+1):
        print("2",end=" ")
    print()
for i in range(1,r+1):
    # x=x+1
    for j in range(1,i+1):
        print("3",end=" ")
    print()
for i in range(r,1,-1):
    for j in range(1,i+1):
        print("4",end=" ")
    print()

