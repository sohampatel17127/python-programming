def recgcd(n, d):
  
   
    if n%d == 0:
        return d
   
    else:
        return recgcd(d, n % d)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = recgcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {result}")