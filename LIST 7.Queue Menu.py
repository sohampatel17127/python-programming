queue=[]

print("-------Queue Menu -------")
print("1. Enqueue (Add)")
print("2. Dequeue (Remove)")
print("3. Display")
print("4. Front")
print("5. Rear")
print("6. Size")
print("7. Exit")

while True:   
    choice=int(input("entre th echoice : "))
    
    
    if choice==1:
        val=input("entre the value : ")
        queue.append(val)
        print("added :",queue)
        
    elif choice == 2:
        if len(queue) == 0:
            print("Queue empty!")
        else:
            removed = queue.pop(0)
            print("Removed:", removed)
            print("Queue:", queue)
        
    elif choice == 3:
        if len(queue) == 0:
            print("Queue empty!")
        else:
            print("Queue:", queue)
            
    elif choice == 4:
        if len(queue) == 0:
            print("Queue empty!")
        else:
            print("Front:", queue[0])
            
    elif choice == 5:
        if len(queue) == 0:
            print("Queue empty!")
        else:                              #last element
            print("Rear:", queue[-1])
            
    elif choice == 6:
        print("Size:", len(queue))
        
    elif choice == 7:
        print("Exiting...")
        break
        
    else:
        print("Invalid choice! (1-7)")
    