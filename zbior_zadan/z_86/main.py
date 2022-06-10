data = []

with open("dane_wybory.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix("\n")
        line = line.split(" ")
        data.append(line)

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

result = list(zip(*result))
result = result[1:len(result)]
for i in result:
    print(sum(i))

state_votes = []
for i in range(0, len(data), 5):
    votes = data[i:i+5]
    votes = list(zip(*votes))
    votes = votes[1:len(votes)]
    votes = [[int(y) for y in x] for x in votes]
    state_votes.append([sum(x) for x in votes])

result = []
for row in state_votes:
    votes = row
    given_mandates = [0 for i in range(5)]
    mandates = 100
    while mandates > 0:
        w = []
        for i in range(5):
            w.append(votes[i] / (2 * given_mandates[i] + 1))
        choosen = w.index(max(w))
        given_mandates[choosen] += 1
        mandates -= 1

    result.append(given_mandates)
print("\n")
result = list(zip(*result))

for i in result:
    print(sum(i))