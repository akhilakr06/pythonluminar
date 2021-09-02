str = input("Enter String:")
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
res = ""
len_str = len(str)
for i in range(len_str):
    if str[i] not in vowel:
        res = res + str[i]

print(res)
