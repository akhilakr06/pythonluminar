n1=int(input("enter num"))
n2=int(input("enter num"))
if n2>n1:
    raise Exception ("num2 is greater")
else:
    print(n1/n2)
# try:
#     c=n1/n2
#     print(c)
# except Exception as  e:
#     # print("divide by 0 not posssible")
#     print(e.args)