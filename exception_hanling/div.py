n1=int(input("enter num"))
n2=int(input("enter num"))
try:
    c=n1/n2
    print(c)
except Exception as  e:
    # print("divide by 0 not posssible")
    print(e.args)