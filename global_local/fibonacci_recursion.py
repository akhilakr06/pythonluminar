def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+ fib(n-2)

nlimit=10

print("fibonnacii series")
for i in range(nlimit):
    print(fib(i))
