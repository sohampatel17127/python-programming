def recsod(n):
    if n == 0:
        return 0
    else:
        return n % 10 + recsod(n // 10)

n = int(input("Enter the number: "))


if n < 0:
    print("Please enter a positive number")
else:
    result = recsod(n)
    print(f"Sum of digits of {n} is: {result}")
    
    