gp={"sugar":80,"rice":90,"weat":60}
gq={"sugar":1,"rice":6,"weat":10}
totalbill=0
for k,v in gp.items():
    for g,q in gq.items():
        if k==g:
            totalbill+=v*q
            
print("Total Bill is :",totalbill)
      