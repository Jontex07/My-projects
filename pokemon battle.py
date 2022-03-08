import random
metrix = []
for i in range(4):
    metrix.append([])
    for j in range(4):
        metrix[i].append(random.randint(0,7))

for row in metrix:
    print(row)

duble = []

def mul(lst,row,col):
    if row <=3:
        return lst[row][col]*mul(lst,row+1,col+1)
    if row >3:
        return 1


print(mul(metrix,0,0))