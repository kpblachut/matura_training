from math import ceil
from secrets import randbelow


data1 = []

with open('dane_systemy1.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data1.append(int(line[1], 2))


result = 0
for i in range(len(data1) - 1):
    for j in range(i + 1, len(data1)):
        r = pow(data1[i] - data1[j], 2)   
        days_beetwen = abs(i - j)
        if ceil(r / days_beetwen) > result:
            result = ceil(r / days_beetwen)


print(result)