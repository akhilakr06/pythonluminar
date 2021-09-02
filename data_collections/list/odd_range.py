# s=100
# n=200
even=[s for s in range(100,200+1) if s%2==0]
print(even)
odd=[s for s in range(100,200+1) if s%2!=0]
print(odd)

# start, end = 10, 29
# # iteration
# for num in range(start, end + 1):
#    # check
#    if num % 2 == 0:
#       print(num, end = " ")