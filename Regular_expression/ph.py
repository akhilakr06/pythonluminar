import re

# x = input("enter")
f1=open("ph_num",'r')

x = "[+][9][1]\d{10}$"
# def check(email):
for num in f1:
    # print(num)
    number=num.rstrip("\n")
    # print(number)
    match = re.fullmatch(x,number)
# if (re.fullmatch(regex, email)):
    if match is not None:
        print(num)

