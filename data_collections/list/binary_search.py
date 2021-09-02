# even=[s for s in range(100,200+1) if s%2==0]
# print(even)
# a=[1,7,5,2,9,3]
# b=[1,2,3,5,7,9]
# mid element find
#
# a=[1,2,3,4,5,6]
# a[0]=4
# print(a)


lst=[1,2,3,4,5,6,7,8,9]
def binsearch():
    lst.sort()
    print(lst)
    ele=int(input("enter the element:"))
    flag=0
    low=0
    upp=len(lst)-1
    print(upp)
    while low<=upp:
        mid=(low+upp)//2
        print(mid)
        if ele > lst[mid]:
            low=mid+1
        elif ele < lst[mid]:
            upp=mid-1
        elif ele==lst[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("not found")

binsearch()