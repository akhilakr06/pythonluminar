import re
x=input("enter")
# regex = "(^|^A)(\S+)(B$|$)"
regex = "^a[a-zA-Z0-9\W]*b$"
# def check(email):
match=re.fullmatch(regex,x)
# if (re.fullmatch(regex, email)):
if match is not None:
    print("Valid ")
else:
    print("Invalid")