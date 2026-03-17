name=str(input("Enter the string for name:"))
def palindrome(name):
    if name==name[::-1]:
        print("palindrome :")
    else:
        print("no")
        
palindrome(name)
        