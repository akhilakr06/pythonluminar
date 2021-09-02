# lst=[2,4,6] #[10,8,6]
# lst=[3,5,7] #[12,10,8]


# sum of pairs
lst=[2,3,4,5]

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==6):
            print(lst[i],lst[j])

