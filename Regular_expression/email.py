import re
email=input("enter email id:")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# def check(email):
match=re.fullmatch(regex,email)
# if (re.fullmatch(regex, email)):
if match is not None:
    print("Valid Email")
else:
    print("Invalid Email")











#
# if __name__ == '__main__':
#     email = "ankitrai326@gmail.com"
#     check(email)
#     email = "my.ownsite@our-earth.org"
#     check(email)
#     email = "ankitrai326.com"
#     check(email)
