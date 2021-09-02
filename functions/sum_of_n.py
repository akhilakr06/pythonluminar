#sum of n


def sum(n):
    s = 0
    if n>0:
        for i in range(1,n+1):
            s=s+i
        print(s)
    else:
        print("enter a =ve number")
sum(5)