name=str(input("Enter the perfact string :"))
def ispangram(name):
    alphabet=set("abcdefghijklmnopqrstuvwxyz")
    lower=name.lower()
    result=set(lower)
    if alphabet.issubset(result):
        return True
    else:
        return False


if ispangram(name):
    print("YES pangram")
else:
    print("NOT a pangram.")