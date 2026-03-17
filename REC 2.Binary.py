
num = int(input("Enter a decimal number: "))

def binary(n):
   
    if n <= 1:
        return str(n)
    
    
    return binary(n // 2) + str(n % 2)


result = binary(num)
print(f"Binary of {num} is: {result}")