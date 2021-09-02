lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
print("orginal Lsit:",lst)
res=[]
for i in lst:
    if i not in res:
        res.append(i)
print("After delete :",res)