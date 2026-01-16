l=int(input("Enter the length"))
w=int(input("Enter the width"))
p=2*(l+w)
a=l*w
print(p)
print(a)
if a>p:
    print("Area is greater than perimetre")
elif p>a:
    print("Perimeter is greater than area")
else:
    print("Both equal")
