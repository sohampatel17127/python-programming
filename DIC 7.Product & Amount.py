d1 = {101: 500, 102: 300, 103: 700, 104: 200}
d2 = {102: 400, 104: 100, 105: 600, 106: 800}
#1
merge={**d1,**d2}
print("baisc merge is :",merge)
#2
for k,v in d1.items():
    for k1,v1 in d2.items():
        if k==k1:
         merge[k]=v+v1
            
print("final merge is here : ",merge)

#3
maxS=max(merge.values())
for prod, sale in merge.items():
    if sale == maxS:
        print(" Top:", prod, "Amount ", sale)
        break
    
#4
import operator
sort=sorted(merge.items(), key = operator.itemgetter(1),reverse=True)
sorted_dict=dict(sort)
print(sorted_dict)