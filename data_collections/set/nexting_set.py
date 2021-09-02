# a={1,2,{3,4}}
# print(a)

set1={1,2,3,4,5,6,7,8,11,32,43,51,22,43,66,12,45}
odd=set()
even=set()
print(set1)
for i in set1:
    if i % 2 == 0:
        # print(i,end=" ")
        odd.add(i)
    else:
        even.add(i)
print("Odd numbers",odd)
print("even numbers",even)