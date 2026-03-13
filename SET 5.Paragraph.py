print("This is the first paragraph :")
para1=input("Enter the first paragraph:")
words=para1.split()
set1=set(words)

print("This is second paragraph:")
para2=input("Entre the second paragraph:")
words=para2.split()
set2=set(words)

uniqueset=(set1|set2)
print("Total",len(uniqueset),"Unique Words.")
print(uniqueset)

print("Common Words:")
print(set1 & set2)