m1 = float(input("Subject 1 marks: "))
m2 = float(input("Subject 2 marks: "))
m3 = float(input("Subject 3 marks: "))

total = m1 + m2 + m3
average = total / 3

#subject 1
if m1 <= 39:
    g1 = "F"
elif m1 <= 44:
    g1 = "P"
elif m1 <= 49:
    g1 = "C"
elif m1 <= 54:
    g1 = "B"
elif m1 <= 59:
    g1 = "B+"
elif m1 <= 69:
    g1 = "A"
elif m1 <= 79:
    g1 = "A+"
else:
    g1 = "O"

#subject 2
if m2 <= 39:
    g2 = "F"
elif m2 <= 44:
    g2 = "P"
elif m2 <= 49:
    g2 = "C"
elif m2 <= 54:
    g2 = "B"
elif m2 <= 59:
    g2 = "B+"
elif m2 <= 69:
    g2 = "A"
elif m2 <= 79:
    g2 = "A+"
else:
    g2 = "O"

#subject3 3
if m3 <= 39:
    g3 = "F"
elif m3 <= 44:
    g3 = "P"
elif m3 <= 49:
    g3 = "C"
elif m3 <= 54:
    g3 = "B"
elif m3 <= 59:
    g3 = "B+"
elif m3 <= 69:
    g3 = "A"
elif m3 <= 79:
    g3 = "A+"
else:
    g3 = "O"

print("\nGrades")
print(f"Subject 1: {m1} = {g1}")
print(f"Subject 2: {m2} = {g2}")
print(f"Subject 3: {m3} = {g3}")

print("\nTotal:",total)
print("\nAverage:",average)

# Pass/Fail check
if m1 <= 39 or m2 <= 39 or m3 <= 39:
    print("Result: Fail")
else:
    print("Result: Pass")

