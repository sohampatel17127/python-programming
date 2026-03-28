def fun():
    print("function inside fun")
def disp():
    print("display inside disp")
def msg():
    print("msg inside msg")
       
lst=[fun,disp,msg]
for f in lst:
    f()
    