import random
lst=[random.randrange(-15,15) for i in range (10)]
print(lst)

squre=list(map(lambda x : x*x,lst))

print(squre)