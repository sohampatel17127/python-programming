name=str(input("Enter the string:"))
def countlu(name):
    digcount=0
    alcount=0
    for char in name :
        if char.isdigit():
            digcount+=1
        elif char.isalpha():
            alcount+=1
    return {"uppercase": digcount, "lowercase": alcount} 



output=countlu(name)
print("Here is ans :",output)