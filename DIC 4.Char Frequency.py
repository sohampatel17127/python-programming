text=input("Enter the string:")
chardic={}
for char in text:
    chardic[char]=text.count(char)
print("Our Result Is Here:",chardic)
    