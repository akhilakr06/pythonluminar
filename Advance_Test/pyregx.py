# import re
# def match(text):
#         x = '[A-Z]+[a-z]+$'
#         if re.search(x, text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
# print(match("AaBbGg"))
# print(match("python"))

import re
x=input("enter")
regex = "^[A-Z]+[a-z]+$"
match=re.fullmatch(regex,x)
if match is not None:
    print("Valid ")
else:
    print("Invalid")
