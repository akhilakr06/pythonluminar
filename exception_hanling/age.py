age=int(input("enter age:"))
if age>=18:
    print("your eligible for vaccination")
else:
    raise Exception ("not eligible for vaccination")