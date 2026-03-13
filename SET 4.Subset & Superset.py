set1=set()
n1=int(input("How many numbr for s1:"))
for i in range(n1):
    i=input("Entre the number for forming set:")
    set1.add(i)
print("Set1 is here :",set1)

set2=set()
n2=int(input("How many nubners for s2:"))
for i in range(n2):
    i=input("Entre the number for forming set:")
    set2.add(i)
print("set2 is here :",set2)

if set1 == set2:
    print("Both sets are equal")
elif set1 <= set2:
    print("Set1 is a subset of set2")
elif set1 >= set2:
    print("Set1 is a superset of set2")
else:
    print("Sets are different")
