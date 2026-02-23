employies={1:[(100,20000),(101,19000),(102,30000)],
           2:[(200,28000),(201,24000),(202,54000)],
           3:[(300,31000),(301,21000),(302,12000)]}

for k,v in employies.items():
    salarys=[]
    for roll_no,salary in v:
        salarys.append(salary)
        
    print("dept no:",k ,"max salary is :",max(salarys))
    print("dept no:",k ,"min salary is :",min(salarys))
        