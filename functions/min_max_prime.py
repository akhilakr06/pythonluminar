#2,3,5,7,11

# min= int(input("enter min number"))
# max= int(input("enter max number"))

min = int(input("Enter minimum number: "))
max = int(input("Enter maximum number: "))

for num in range(min, max + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)