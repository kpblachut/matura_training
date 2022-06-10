data = []

with open("dane_wybory.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix("\n")
        line = line.split(" ")
        data.append(line)

# print(*data, sep="\n")
result = []
for row in data:
    votes = row[1:len(row)]
    votes = [int(i) for i in votes]
    given_mandates = [0 for i in range(5)]
    mandates = 20
    while mandates > 0:
        w = []
        for i in range(5):
            w.append(votes[i] / (2 * given_mandates[i] + 1))
        choosen = w.index(max(w))
        given_mandates[choosen] += 1
        mandates -= 1

    result.append([row[0], *given_mandates])

print(*result, sep="\n")
result = list(zip(*result))
for i in result:
    print(max(i))

