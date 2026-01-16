a=90
b=80
c=45
if a>b and a>c:
    largest = a
elif b>c and b>a:
    largest = b
else:
    largest = c


if a<b and a<c:
    smallest = a
elif b<a and b<c:
    smallest = b
else:
    smallest = c



print("Largest is:",largest)
print("Smallest is:",smallest)
