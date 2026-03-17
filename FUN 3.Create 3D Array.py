n=int(input("Entre the number :"))

def create_array(a,b,c,n):
    array=[]
    for i in range(a):
        width=[]
        for j in range(b):
            row=[]
            for k in range(c):
                row.append(n)
            width.append(row)
        array.append(width)
    return array


output=create_array(3,4,5,n)
print(output)