import random
list=[random.randrange(-50,51) for i in range(30)]
print(list)

poslist=[]
for num in list:
    if num>0:
        poslist.append(num)
        
print("poslist : ",poslist)

neglist=[]
for num in list:
    if num<0:
        neglist.append(num)
        
print("neglist : ",neglist)

zerolist=[]
for num in list:
    if num==0:
        zerolist.append(num)
        
print("zerolist : ",zerolist)