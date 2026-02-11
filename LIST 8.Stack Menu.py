stack = []

print("\n--- STACK MENU ---")
print("1. Push (Add)")
print("2. Pop (Remove)")
print("3. Display")
print("4. Top")
print("5. Size")
print("6. Exit")
while True:  
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        val = input("Enter value: ")
        stack.append(val)
    
        print("Stack:", stack)
        
    elif choice == 2:
        if len(stack) == 0:
            print("Stack empty!")
        else:
            removed = stack.pop()
            print("Popped:", removed)
            print("Stack:", stack)
            
    elif choice == 3:
        if len(stack) == 0:
            print("Stack empty!")
        else:
            print("Stack:", stack)
            
    elif choice == 4:
        if len(stack) == 0:
            print("Stack empty!")
        else:
            print("Top:", stack[-1])
            
    elif choice == 5:
        print("Size:", len(stack))
        
    elif choice == 6:
        print("Exiting...")
        break
        
    else:
        print("Invalid choice! (1-6)")