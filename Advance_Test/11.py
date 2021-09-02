import re
x=input("enter")
regex = "[A-Z]+[a-zA-z0-9]{3,8}[A-Z]"
match=re.fullmatch(regex,x)
if match is not None:
    print("Valid ")
else:
    print("Invalid")

