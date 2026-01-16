x=float(input("Enter x:"))
y=float(input("Enter y:"))
print("Circle center is =",x  ,  y)
r=float(input("Enter radius"))
x1=float(input("Enter random x1"))
y1=float(input("Entre random y1"))
A=pow(x1-x,2)
B=pow(y1-y,2)
result=pow(A+B,1/2)
if(result<r):
    print("inside")
elif(result>r):
    print("outside")
else:
    print("on circle")


