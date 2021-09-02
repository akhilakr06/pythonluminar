#even numbers between min and max

# min=int(input("enter min number"))
# max=int(input("enter max number"))
# for i in range(min,max+1):
#     if(i%2==0):
#         print(i)
#         #i=i+1
#


min=int(input("enter min num:"))
max=int(input("enter max num:"))

while min<=max:
    if min % 2==0:
        print(min)
    #min=min+1
    min+=1