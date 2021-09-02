#set tp store elements

# a={2,3,4,5}
# print(a)
# print(type(a))
#

a=set()
a.add(2)
a.add(4)
a.add(7)
print(a)

b={9,7,5,1,2}
print(b)
c=a&b
print(c)
d=a|b
print(d)
# 1.order doesnt keep
# 2.heterogeneous
# 3.not support duplicate elements
# 4. mutable....updating possible
# 5. nexting is not possible


