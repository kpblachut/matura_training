data = []

with open('galerie.txt', 'r') as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split(" ")
        data.append(line[0])

unique = list(set(data))

for i in unique:
    print(i , data.count(i))

