# s=[]
# a=[1,2,3,4,5,6,7,8,9]
#
# for i in a:
#     b=i*5
#     s.append(b)
# print(s)
# #
# list comprehension
a=[1,2,3,4,5,6,7,8,9]
s=[n*5 for n in a]
print(s)
