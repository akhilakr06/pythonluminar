string= input("enter a string")
unwanted="<>!@#&.,()^*$%"
# for i in unwanted:
#     string= string.replace(i,"")
# print(string)
# #
c=""
for i in string:
    if i not in unwanted:
        c=c+i
print(c)
