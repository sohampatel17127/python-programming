list1 = []
list2 = []

n1 = int(input("Enter number of elements in list 1: "))
for i in range(n1):
    num = int(input(f"Enter element  for list 1: "))
    list1.append(num)

n2 = int(input("Enter number of elements in list 2: "))
for i in range(n2):
    num = int(input(f"Enter element  for list 2: "))
    list2.append(num)
    
    
    
print(f"List 1: {list1}")
print(f"List 2: {list2}")


def intersection(list1, list2):
    result = []
    
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in result:
                result.append(item1)
                break
    
    return result


common = intersection(list1, list2)

print(f" Common elements: {common}")