name=str(input("Enter ths string :"))

def frequency(name):
    words=name.split()
    strdic={}
    for word in words:
        strdic[word]=words.count(word)
        
    sorteddict=dict(sorted(strdic.items()))
    
    print("Our Result Is Here:",sorteddict)
    
    
frequency(name)
    
    