# string=input("Enter string:")
# vowels=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)

str=input("enter string:")
c=0
#v="aeiou"

for i in str:
    if i in 'aeiou':
        c+=1
print("number of vowels are:",c)