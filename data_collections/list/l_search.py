lst=[1,2,3,4,5,77,88,41,45]
def linsearch(lst):
    ele=int(input("enter elements to search"))
    f=0
    for i in lst:
        if i==ele:
            f=1
            break
    if f==0:
        print("not found")
    else:
        print("found")
linsearch(lst)