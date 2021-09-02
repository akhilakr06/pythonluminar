def patt(n):
    # num=1
    for i in range(1,n):
        for j in range(1,i):
            print(j,end=" ")
            # num+=1

        print()

patt(6)