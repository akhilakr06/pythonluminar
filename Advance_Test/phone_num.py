import re
f1=open("phn",'r')
x = "[+][9][1]\d{10}$"
for num in f1:
    number=num.rstrip("\n")
    match = re.fullmatch(x,number)
    if match is not None:
        print(num)

