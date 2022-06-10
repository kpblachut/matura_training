data1 = []

with open('dane_systemy1.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data1.append(int(line[1], 2))

print(bin(min(data1)))

data2 = []

with open('dane_systemy2.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data2.append(int(line[1], 4))

print(bin(min(data2)))

data3 = []

with open('dane_systemy3.txt', 'r') as file:
    for line in file.readlines():
        line = line.split()
        data3.append(int(line[1], 8))

print(bin(min(data3)))
        
