n = int(input("n: "))
r = int(input("r: "))

npr = 1
ncr = 1

for i in range(r):
    npr *= (n - i)
    ncr = ncr * (n - i) // (i + 1)

print(f"nPr = {npr}")
print(f"nCr = {ncr}")