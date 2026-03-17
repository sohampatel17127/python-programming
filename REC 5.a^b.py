def power(a, b):
    
    if b == 0:
        return 1
    
    elif b == 1:
        return a
    
    else:
        return a * power(a, b - 1)


a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))

result = power(a, b)
print(f"{a}^{b} = {result}")