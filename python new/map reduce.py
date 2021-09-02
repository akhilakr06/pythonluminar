lst=[2,3,4,5,6]

def square(num):
    return num
evens=list(filter(lambda num:num%2==0,lst))
print(evens)
# square of all nos

# map(function,lst/iterable)
# def square(num):
#     return num**2
# squares=list(map(square,lst))
# print(squares)
#
#
# cubes=list(map(lambda num:num**3,lst))
# print(cubes)
# squares=list(map(lambda num:num**2,lst))
# print(squares)


# filter
# filter(function,iterable)

def check_even():
    return num%2==0

evens=filter(check_even(),lst)
print(evens)