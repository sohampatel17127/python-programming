sub1=int(input("Enter first marks :"))
sub2=int(input("Enter second marks :"))
sub3=int(input("Enter third marks :"))
sub4=int(input("Enter fourth marks :"))
sub5=int(input("Enter five marks :"))



def avg(sub1,sub2,sub3,sub4,sub5):
    total=sub1+sub2+sub3+sub4+sub5
    avg=total/5
    print(avg)
    print(total)
    
avg(sub1,sub2,sub3,sub4,sub5)