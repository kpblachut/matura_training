def dividers(num):
    dividers = []
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            dividers.append(i)
    dividers.append(num)

    return dividers

data = []

with open("liczby.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        data.append(int(line))

result = []
for num in data:
    divs = dividers(num)
    if len(divs) == 18:
        result.append(divs)

for i in result:
    print(f"{i[-1]}, {sorted(i)}")

