n=int(input("enter the  limit"))

def sum_prime(n):
    sum=0
    for i in range(2,n+1):
        j=2
        for j in range(2,i):
            if (i%j)==0:
                j=i
                break
        if j is not i:
            sum+=i
    print("sum of prime numbers up to 50:",sum)
sum_prime(n)
# l=1
# u=50
# for num in range(1,u+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)