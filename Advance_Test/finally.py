
a=5
b=0
try:
    c=a/b
except(ZeroDivisionError):
    print("cant divide by 0")
finally:
    print("This code is executed")