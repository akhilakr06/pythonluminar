lst=[2,3,4,5]
# total=7
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==7):
            print(lst[i],lst[j])
