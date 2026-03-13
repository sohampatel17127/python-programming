d1={109,110,111,113,114,234,209}
d2={109,112,121,113,290}

print("Visitors id is here where d1 stand day 1 and d2 stand where day2:")
print(d1)
print(d2)

print("Who come for two days :")
print(d1 & d2)

print("Total unique visitors:")
print(d1|d2)

print("Visitors who come only for one day:")
print(d1^d2)