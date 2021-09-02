# c=1
# s=2
# r=3
#
# for i in range(r):
#     for col in range(1,s):
#         print(c,end=" ")
#         c+=1
#     print(" ")
#     s+=2

def patt(n):
    num=1
    for i in range(0,n): #i=0,1
        for j in range(i): #j=0,1
            print(num,end=" ")
            num=num+1   #num=2
        print( )
patt(5)