name=str(input("ENTER THE NAME"))
print("Your string is : ",name)


l=len(name)
print("Length is :",l)

last_character = name[-1]
print("LAST character is : ",last_character)

first=name[0]
print("FIRST character is : ",first)

l=len(name)

if(l%2==0):
     print("THIS IS EVEN STRING")
   
else:
    m=name[l//2]
    print("MIDDLE is : ",m)