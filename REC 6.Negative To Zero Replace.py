lst = []
for i in range(5):
    num = int(input("Enter the value: "))
    lst.append(num)

def sanitize_list(lst, index=0):
    
    if index == len(lst):
        return lst
    else:
        
        if lst[index] < 0:
            lst[index] = 0  
        return sanitize_list(lst, index + 1)


sanitize_list(lst)
print("Sanitized list:", lst)
            