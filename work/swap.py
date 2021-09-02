#Swap two numbers
# # x=20
# # y=10
# x= int(input("x value:"))
# y= int(input("y value:"))
# print("Before Swapping values",x,y)
# # x,y=y,x
# t=x
# x=y
# y=t
# print("After Swapping values",x,y)
# #second approach
# x= int(input("x value:"))
# y= int(input("y value:"))
# print("Before Swapping values",x,y)
# # x,y=y,x
# print("After Swapping values",x,y)
# #third approach

x= int(input("x value:"))
y= int(input("y value:"))
print("Before Swapping values",x,y)
x=x+y
y=x-y
x=x-y
print("After Swapping values",x,y)