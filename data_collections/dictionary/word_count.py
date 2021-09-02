# str="hello hi hello"
# hello:2
# hi:1
# string = input("Please enter any String : ")
# words = []
#
# words = string.split()
# frequency = [words.count(i) for i in words]
#
# myDict = dict(zip(words, frequency))
# print("Dictionary Items  :  ",  myDict)

count={}
data=input("enter")
words=data.split(" ")
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val+=1
        count.update({word:val})
    print(count)



