# row=5
# for i in range(row+1):
#     for j in range(i):
#         print(i,end=" ")
#     print('')
# for i in range(row+1):
#     for j in range(i):
#         print(i,end=" ")
#     print('')
#

a=int(input("initial value"))
b=int(input("final value"))
r=5
for i in range(a,b):
    if(i%2==0):
        for k in range(r,0,-1):
            for j in range(0,k):
                print(i,end=" ")
            print()
    else:
        for l in range(r):
            for m in range(0,l+1):
                print(i,end=" ")
            print()