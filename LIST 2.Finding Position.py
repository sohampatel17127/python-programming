import random
list=[random.randrange(1,21) for i in range(20)]
print("list : ",list)

search=int(input("enterthe number for search : "))

positions = []
for i in range(20):
    if list[i] == search:
        positions.append(i)
        
if len(positions) == 0:
    print("not found",search)
else:
    print(search, "'S positions:", positions)
    print("Total", len(positions), "times repeat")