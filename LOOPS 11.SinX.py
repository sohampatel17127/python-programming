# User se radians input lo
x = float(input("Radians: "))

# Variables set karo
answer = 0
sign = 1

# 10 terms ke liye loop chalao
for n in range(10):
    # x ki power nikaloo
    power = 1
    for i in range(2*n + 1):
        power = power * x
    
    # Factorial nikaloo
    fact = 1
    for i in range(1, 2*n + 2):
        fact = fact * i
    
    # Term add karo
    term = sign * power / fact
    answer = answer + term
    
    # Sign change karo
    sign = -sign

# 4. Answer print karo
print(f"sin({x}) = {answer}")