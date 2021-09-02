def fact(num):
    f = 1
    if num>0:
    #num=int(input("number:"))

        for i in range (1,num+1):
            f=f*i
        print(f)
    elif num == 0:
        print("factorial of 0 is 1")
    else:
        print("doesnt exist for -ve numbers")

fact(5)
fact(-1)
fact(0)


