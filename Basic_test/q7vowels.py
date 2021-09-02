str=input("enter string:")
str.lower()
out=""
vowels='aeiou'
str_len=len(str)
for i in str_len:
    if str not in vowels:
        # str=str.replace(i," ")
        out=out+str[i]
print(out)
