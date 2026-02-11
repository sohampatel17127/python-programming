term=int(input("how many terms:"))
frlist=[]
for i in range(term):
    i=float(input("fernhit : "))
    frlist.append(i)
    
cellist=[]
for j in frlist:
     c = (j - 32) * 5/9
     cellist.append(round(c, 2))
    
print("cellist :",cellist)