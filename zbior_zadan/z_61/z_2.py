data = []
import math


with open("ciagi.txt", "r") as file:
    lines = file.readlines()
    for i in range(1, len(lines), 2):
        line = lines[i].removesuffix("\n")
        data.append(line.split())

result = []
for seq in data:
    seq = [int(i) for i in seq]
    temp = []
    for num in seq:
        if int(round(num ** (1/3))) ** 3 == num :
            temp.append(num) 

    if temp:
        result.append(max(temp))
            

for i in result:
    print(i)

