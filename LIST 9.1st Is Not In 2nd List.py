lst1=[]
n1=int(input("enter the terms for list1 : "))
for i in range(n1):
    num=int(input(f"entre the number{i+1} :"))
    lst1.append(num)
    
lst2=[]
n2=int(input("enter the terms for list2 : "))
for i in range(n2):
    num=int(input(f"entre the number{i+1} :"))
    lst2.append(num)
    
    
lst3=[x for x in lst1 if x not in lst2 ]

print("list 3 : ",lst3)