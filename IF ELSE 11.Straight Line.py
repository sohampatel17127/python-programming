x1=float(input("enter the number x1"))
y1=float(input("enter the number y1"))
x2=float(input("enter the number x2"))
y2=float(input("enter the number y2"))
x3=float(input("enter the number x3"))
y3=float(input("enter the number y3"))
if ((x3-x2)==0 or (x2-x1)==0):
    if x1==x2==x3:
        print("vertical straight line")
    else:
        print("undefined")
else:
    slop1=(y3-y2)/(x3-x2)
    slop2=(y2-y1)/(x2-x1)
    if slop1==slop2:
        print("this three points are in one straight line")
    else:
        print("this three points are not in one straight line")
