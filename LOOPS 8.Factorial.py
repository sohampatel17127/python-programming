n=int(input("entre the number for factorial : "))
factorial=1
for i in range(n):
    factorial *=n
    n-=1
print("factorial is this = ",factorial)