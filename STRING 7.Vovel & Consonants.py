name=str(input("ENTER THE NAME"))
print("This is your string : ",name)

print("Count of vovel")
a= name.count('a')
e = name.count('e')
i = name.count('i')
o = name.count('o')
u = name.count('u')

print("Number of a is =",a)
print("Number of e is =",e)
print("Number of i is =",i)
print("Number of o is =",o)
print("Number of u is =",u)

total_vovel=a+e+i+o+u
print("Total vovel is here : ",total_vovel)

length=len(name)
print("String length is here :",length)

con=length-total_vovel
print("Count of consonants is : ",con)