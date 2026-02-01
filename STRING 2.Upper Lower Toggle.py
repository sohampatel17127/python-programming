
name = str(input("ENTER THE NAME FOR STRING : "))
#result ko stor karne ke liye empty strings
U = ""  # UPPERCASE
L = ""  # lowercase  
T = ""  # TOGGLE


for c in name:
    # Lowercase है (a-z)
    if 'a' <= c <= 'z':
        U = U + chr(ord(c) - 32)  # UPPERCASE (-32)
        L = L + c                 # lowercase (same)
        T = T + chr(ord(c) - 32)  # TOGGLE (-32)
    
    # Uppercase है (A-Z)
    elif 'A' <= c <= 'Z':
        U = U + c                 # UPPERCASE (same)
        L = L + chr(ord(c) + 32)  # lowercase (+32)
        T = T + chr(ord(c) + 32)  # TOGGLE (+32)
    
    # Other characters
    else:
        U = U + c
        L = L + c
        T = T + c


print("\nResults:")
print("UPPER:", U)
print("lower:", L)
print("TOGGLE:", T)
