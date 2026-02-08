print("PRIME NUMBER:")

n=int(input("enter the number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
                
if count==2:
    print("prime:")
else:
    print("not prime")

print("\n\n")
print("PALINDROME:")

name=str(input("enter the string name :"))
print(name)
pal=name[::-1]
if pal==name:
    print("palindrome")
else:
    print("not palindrome")
    
print("\n\n")
print("PERFACT:")

num=int(input("enter the number :"))
original=num
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
                       
if sum==original:
    print("yes perfact")
else:
    print("not perfact")
 
print("\n\n") 
print("AUTOMORPHIC:")
    
    
num = int(input("enter the number : "))
original = num
square = num * num

num_str = str(original)
square_str = str(square)

if square_str.endswith(num_str):
    print("yes automorphic")
else:
    print("not automorphic")

print("\n\n")
   
print("ARMSTRONG:")
num = int(input("enter the number: "))
originalnum = num
sum = 0

while num > 0:
    digit = num % 10
    num = num // 10  # Integer division in Python
    sum = sum + (digit * digit * digit)

print(f"sum = {sum}")

if sum == originalnum:
    print("armstrong number")
else:
    print("not armstrong number")