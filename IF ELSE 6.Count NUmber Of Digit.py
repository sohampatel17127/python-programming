num = int(input("Enter number (0 to 99999): "))
num = abs(num)

if num < 10:
    print("1 digit")
elif num < 100:
    print("2 digits")
elif num < 1000:
    print("3 digits")
elif num < 10000:
    print("4 digits")
elif num < 100000:
    print("5 digits")
else:
    print("More than 5 digits")
