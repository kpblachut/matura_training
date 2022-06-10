data1 = []

with open('dane_systemy1.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data1.append(int(line[1], 2))

record = data1[0]
days1 = []
for day, tmp in enumerate(data1):
    if tmp > record:
        record = tmp
        days1.append(day)

data2 = []

with open('dane_systemy2.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data2.append(int(line[1], 4))

record = data2[0]
days2 = []
for day, tmp in enumerate(data2):
    if tmp > record:
        record = tmp
        days2.append(day)

data3 = []

with open('dane_systemy3.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data3.append(int(line[1], 8))


record = data3[0]
days3 = []
for day, tmp in enumerate(data3):
    if tmp > record:
        record = tmp
        days3.append(day)

result = list(set(days1 + days2 + days3))

print(len(result) + 1)

