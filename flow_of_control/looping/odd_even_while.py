#2,4,6,8
#1,3,5,7
#odd even
#%2==0 even

num=int(input("number:"))
# i=0
# while i>0:
if num>0:
    if(num %2==0):
        print("even number")
    else:
        print("odd  number")
    # i=i+1
else:
    print("enter number is negative")