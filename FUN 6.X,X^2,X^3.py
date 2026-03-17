n=int(input("Enter the number :"))
def convert(n):
    list=[]
    for i in range(1,n+1):
        list.append((i,i*i,i*i*i))
    print(list)
    
    
convert(n)