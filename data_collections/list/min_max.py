lst=[1,2,12,5,24,4,22]
lst.sort()
print(lst[0])
print(lst[-1])
list=[]
n = int(input("Enter the length of your list: "))
for i in range (1,n+1):
    a=int(input("Enter the %d number: " %i ))
    list.append(a)
print(list)
min=list[0]
max=list[0]
for i in range(1,n):
    if max<list[i]:
        max=list[i]
    if min>list[i]:
        min=list[i]
print(" %d is the biggest number " %max)
print(" %d is the smallest number " %min)