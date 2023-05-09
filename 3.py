l1  = [2,4,9,-10,100,1000,89,67,1,3,0,98]
temp = 0
temp2 = 0
temp3 = 0
temp4 = 0
for i in l1:
    for j in range(len(l1)):
        if i > temp:
            temp = i
        else:
            continue

for i in l1:
    for j in range(len(l1)):
        if i > temp2 and i < temp:
            temp2 = i
        else:
            continue

for i in l1:
    for j in range(len(l1)):
        if i < temp3:
            temp3 = i
        else:
            continue

for i in l1:
    for j in range(len(l1)):
        if i < temp4 and i > temp3:
            temp4 = i
        else:
            continue
print("largest",temp)
print("second largest",temp2)
print("samllest",temp3)
print("second smallest",temp4)