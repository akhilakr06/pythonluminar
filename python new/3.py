lst1=[10,11,12,20,21,30]
lst2=[20,21,22,23,24,30]
# find common elements from both list
# one_not_two = [ x for x in lst1 if x not in lst1 ]
# print(one_not_two)
# two_not_one = [ x for x in lst2 if x not in lst2 ]
# print(two_not_one)

common = [x for x in lst1 if x in lst2]
print(common)


