import re
x=input("enter")

regex="^[A-Z]\w{5,10}$"
match=re.fullmatch(regex,x)
if match is not None:
    print("Valid ")
else:
    print("Invalid")
