data = []

with open("ciagi.txt", "r") as file:
    lines = file.readlines()
    for i in range(1, len(lines), 2):
        line = lines[i].removesuffix("\n")
        data.append(line.split())

result = []
for sequence in data:
    sequence = [int(x) for x in sequence]
    isArithmetic = True
    sub = sequence[1] - sequence[0]
    for i in range(0, len(sequence)-2):
        if (sequence[i + 1] != (sequence[i] + sequence[i + 2])/2):
            isArithmetic = False

    if isArithmetic:
        result.append(sub)

print(len(result))
print(sorted(result, reverse=True)[0])
print(result)
