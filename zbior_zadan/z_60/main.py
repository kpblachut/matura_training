def dividers(num):
    dividers = []
    for i in range(2, int(num/2) + 1):
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
allDivs = []

for num in data:
    divs = dividers(num)
    for div in divs:
        allDivs.append(div)

for num in data:
    divs = dividers(num)
    isPrime = True
    for div in divs:
        if allDivs.count(div) > 1:
            isPrime = False
    
    if isPrime:
        result.append(num)

print(sorted(result, reverse=True))
