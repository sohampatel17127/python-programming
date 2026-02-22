sdata=[("soham",109,18),("rani",100,19),("pinku",108,15),("king",108,101)]
name=[]
rollno=[]
age=[]

for student in sdata:
    name.append(student[0])
    rollno.append(student[1])
    age.append(student[2])
    
    
print("ALL NAMES :",name)
print("ALL ROLL NO :",rollno)
print("ALL AGE:",age)