a=[1,23,3]
index=int(input("enee index:"))
try:
    print(a[index])
except Exception as e:
    print(e.args)