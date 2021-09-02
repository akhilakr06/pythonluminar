import re
x=input("enter")

# regex = "^[a-zA-Z]{8,16}$"
regex = "^[\D]{8,16}$"
# def check(email):
match=re.fullmatch(regex,x)
# if (re.fullmatch(regex, email)):
if match is not None:
    print("Valid ")
else:
    print("Invalid")