name1=str(input("ENTER THE FIRST STRING :"))
name2=str(input("ENTER THE SECOND STRING:"))

if(name1 in name2):
    print(f"YES {name1} is in {name2}")
elif(name2 in name1):
    print(f"YES {name2} is in {name1}")
else:
    print("NO , this string is not in another string")