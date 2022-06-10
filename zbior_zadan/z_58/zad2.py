import re


data1 = []

with open('dane_systemy1.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data1.append(int(line[0], 2))

result1  = []
initial_input = data1[0]
for i, data in enumerate(data1):
   if (data-initial_input) % 24 != 0:
    #    print(f"{i} : {data} : {initial_input}")
       result1.append(i + 1)

data2 = []

with open('dane_systemy2.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data2.append(int(line[0], 4))

result2  = []
initial_input = data2[0]
for i, data in enumerate(data2):
   if (data-initial_input) % 24 != 0:
    #    print(f"{i} : {data} : {initial_input}")
       result2.append(i + 1)

data3 = []

with open('dane_systemy3.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data3.append(int(line[0], 8))

result3  = []
initial_input = data3[0]
for i, data in enumerate(data3):
   if (data-initial_input) % 24 != 0:
    #    print(f"{i} : {data} : {initial_input}")
       result3.append(i + 1)

result = list(set(result1).intersection(result2))
result = list(set(result).intersection(result3))

print(len(result))



