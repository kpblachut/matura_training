data = []

with open('sygnaly.txt') as file:
    for line in file.readlines():
        line = line.removesuffix("\n")
        data.append(line)


result = ""
for i, sig in enumerate(data):
    if (i + 1) % 40 == 0: # Finds every fortieth word
        result += sig[9] # Takes the tenth letter

print(result)
