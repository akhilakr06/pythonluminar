# def printv(*args):
#     return(sum(args))
# print(printv(1,2,3,4,5,6))
def printv(*args):
    s=0
    for i in args:
        s+=1
    return(sum(args))
print(printv(1,2,3,4,5,6))


