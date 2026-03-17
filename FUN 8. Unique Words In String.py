name=str(input("Enter ths string :"))

def convert(name):
    words = name.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    print(sorted_words)
        
convert(name)