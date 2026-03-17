lst=[]
for i in range(5):
    i=int(input("entre the number :"))
    lst.append(i)
    
def calculateavg(lst,index=0,total=0):
     if index==len(lst):
         avg=total/len(lst)
         print("average is :",avg)
     else:
        return calculateavg(lst,index+1,total+lst[index])
        
        
        
calculateavg(lst)