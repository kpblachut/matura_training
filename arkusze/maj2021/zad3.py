instructions = []

with open('instrukcje.txt') as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split(" ")
        if line[0] == "DOPISZ":
            instructions.append(line[1])

print(max(instructions))
print(instructions.count("Z"))



