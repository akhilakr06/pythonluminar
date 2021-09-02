lst=[1,2,3,4,5]
# sum=lst(lower)+lst(upper)
# 5==sum
# sum>5

low=0
upper=len(lst)-1
pair=10
pairs=[]
count=0

# while(low<upper):
#     sum=lst[low]+lst[upper]
#     if(sum==pair):
#         # print(lst[low],lst[upper])
#         pairs.append((lst[low],lst[upper]))
#         low+=1
#         # break
#     elif(sum>pair):
#         upper-=1
#     elif(sum<pair):
#         low+=1
#     count+=1
#
# print(count)


for i in lst:
    for j in lst:
        if(i!=j):
            if(i+j==pair):
                print(i,j)
        count+=1
print(count)