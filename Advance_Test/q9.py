# import re
# def match(text):
#         patterns = 'a.*?b$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(match("aabbbbd"))
# print(match("aabAbbbc"))
# print(match("accddbbjjjb"))

import re
x=input("enter")
regex = "^a[0-9]+b$"
match=re.fullmatch(regex,x)
if match is not None:
    print("Valid ")
else:
    print("Invalid")
