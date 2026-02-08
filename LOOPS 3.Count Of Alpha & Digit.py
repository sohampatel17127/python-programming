text=str(input("Entre the string : "))
alcount=0
dgcount=0
for char in text:
    if char.isalpha():
     alcount=alcount+1
    elif char.isdigit():
     dgcount=dgcount+1
    
print("\n\n")

print("Total Alphabets = ",alcount)
print("Total Digit =",dgcount)