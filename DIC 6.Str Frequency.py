text=input("Enter the string:")
words=text.split()
strdic={}
for word in words:
    strdic[word]=words.count(word)
print("Our Result Is Here:",strdic)
    