import re
x=input("enter")


regex = "[A-Z][0-9\W]*"
# def check(email):
match=re.fullmatch(regex,x)
# if (re.fullmatch(regex, email)):
if match is not None:
    print("Valid ")
else:
    print("Invalid")
