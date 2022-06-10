from itertools import count
from string import hexdigits


data = []

with open('galerie.txt', 'r') as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split(" ")
        line_data = [line[0], line[1]]
        shops = []
        for i in range(2, len(line), 2):
            if line[i] != '0' :
                shops.append([line[i], line[i+1]])

        line_data.append(shops)
        data.append(line_data)

result = []

for country, city, shops in data:
    pole = 0
    for x, y in shops:
        pole += int(x)*int(y)

    result.append([city, pole, len(shops)])

for row in result:
    for d in row:
        print(d, end=" ")
    print('')

lowest=5000
highest = 0
temph = []
templ = []

for i in result:
    if i[1] < lowest:
        lowest = i[1]
        templ = i
    if i[1] > highest:
        highest = i[1]
        temph = i

print(temph)
print(templ)