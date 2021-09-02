# print("Full Pyramid Pattern of Stars (*): ")
# for i in range(5):
#     for s in range(-6, -i):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


k=6
for i in range(6):
    for r in range(k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()