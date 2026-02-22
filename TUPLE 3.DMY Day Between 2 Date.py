d1,m1,y1=(15,9,2023)
d2,m2,y2=(20,12,2023)
monthdays=[31,28,31,30,31,30,31,31,30,31,30,31]


# Date1 ke total days
days1 = 0
y = 1
while y < y1:
    if y%4==0 and (y%100!=0 or y%400==0):
        days1 += 366
    else:
        days1 += 365
    y += 1
m = 1
while m < m1:
    days1 += monthdays[m-1]
    if m==2 and (y1%4==0 and (y1%100!=0 or y1%400==0)):
        days1 += 1
    m += 1
days1 += d1

# Date2 ke total days
days2 = 0
y = 1
while y < y2:
    if y%4==0 and (y%100!=0 or y%400==0):
        days2 += 366
    else:
        days2 += 365
    y += 1
m = 1
while m < m2:
    days2 += monthdays[m-1]
    if m==2 and (y2%4==0 and (y2%100!=0 or y2%400==0)):
        days2 += 1
    m += 1
days2 += d2

diff = days2 - days1
print(f"{d1}/{m1}/{y1} to {d2}/{m2}/{y2} = {diff} days")
