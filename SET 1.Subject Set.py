st1={"m","p","c"}
st2={"p","b","m"}

print("Subject which is taken only st1 :",st1.difference(st2))
print("Subject which is taken only st2 :",st2.difference(st1))
print("Common subject is here :",st1.intersection(st2))
print("Total unique subjects :",st1.union(st2))