from data_collections.list.demo import list1

list1=[]
limit=int(input("enter limit"))
for i in range(limit):
    elements=int(input("enter element"))
    list1.append(elements)
print(list1)