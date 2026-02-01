name=str(input("ENTER THE NAME"))
print("Your string is here : ",name)

print("Now forward and reverse is here\n")

#forwaod string

i=0
while i<len(name):
    print(f"{name[i]}")
    i+=1
    
print("Reverse string\n")

i=len(name)-1
while i>=0:
  print(f"{name[i]}")
  i-=1
  
"""
  
yaha hum loop ke bina slicing se bhi kar sakte hai 
forwrd ke liye [:end]
reverse ke liye [::-1]

"""