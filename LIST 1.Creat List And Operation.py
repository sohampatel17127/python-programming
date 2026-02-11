import random
oddlist=[random.randrange(1,100,2) for i in range(5)]
print("oddlist : ",oddlist)

evenlist=[random.randrange(2,100,2) for i in range(4)]
print("evenlist : ",evenlist)

oroddlist=oddlist.copy()

oddlist[2:3]= evenlist 
print(oddlist)

Flatternlist = oroddlist+evenlist   # we use oddlist.extend(evenlist) but not any return  = kuch variable nahi banana
print("After flatten:", Flatternlist)

Flatternlist.sort()
print(Flatternlist)







