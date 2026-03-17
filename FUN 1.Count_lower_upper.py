name=str(input("Entre the string:"))
def countlu(name):
    ucount=0
    lcount=0
    for char in name :
        if char.isupper():
            ucount+=1
        elif char.islower():
            lcount+=1
    return {"uppercase": ucount, "lowercase": lcount} 



output=countlu(name)
print("here is ans :",output)