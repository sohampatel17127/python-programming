name = input("Enter the string: ")

def length(str, index=0, count=0):
    # Base case: last character sudhi pohochi gaya
    if index == len(str) - 1:
        count += 1  # Last character count karo
        print("Length is:", count)
        return count
    
    # Current character count karo
    count += 1
    
    # Recursive call for next character
    return length(str, index + 1, count)

length(name)