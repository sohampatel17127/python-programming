food=[("samosa",25),("dabeli",30),("vadapao",20),("bhajipav",100),("pizza",80)]
price=[]
for item in food:
    price.append(item[1])

price.sort(reverse=True)


newfood=[]
for p in price:
    for item in food:
        if item[1]==p:
         newfood.append(item)
        
print(newfood)
