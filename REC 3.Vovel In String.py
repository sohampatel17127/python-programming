name = input("Enter the string: ")

def count_vowels(str, index=0, count=0):
    
    if index == len(str):
        print("Count is:", count)
        return count
    else:
        
        if str[index].lower() in "aeiou":  
            count += 1
        
        return count_vowels(str, index + 1, count)


count_vowels(name)