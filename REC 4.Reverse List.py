lst = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)

def reverse_list(lst):
    
    if len(lst) <= 1:
        return lst
    
    return [lst[-1]] + reverse_list(lst[:-1])


print(f"Reversed: {reverse_list(lst)}") 