data = []

with open("bledne.txt", "r") as file:
    lines = file.readlines()
    for i in range(1, len(lines), 2):
        line = lines[i].removesuffix("\n")
        data.append(line.split())

result = []
for seq in data:
    seq = [int(i) for i in seq]
    sub = seq[1] - seq[0]
    temp = []
    for i in range(len(seq)-1):
        if sub != seq[i + 1] - seq[i]:
            temp.append(seq[i+1])

    print(temp)
            

for i in result:
    print(i)

