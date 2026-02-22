students=[("rahul",),("rani"),("rajesh",),("rinku",)]

boy_count=0
girl_count=0

for i in students:
    if isinstance(i,tuple):
        boy_count+=1
    else:
        girl_count+=1
        
print("number of boys :",boy_count)
print("number of girl :",girl_count)
        
