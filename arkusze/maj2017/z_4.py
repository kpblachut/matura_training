data = []

with open("dane.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split()

        line = [int(x) for x in line] # Converts items to integers
        data.append(line)

data = list(zip(*data)) # Replace rows with colums and colums with rows

# Looks for longest identical sequence in row
result = 1
for line in data:
    temp = 1
    current = line[0]
    for index in range(1, len(line)):
        if current == line[index]:
            temp += 1
        else: 
            current = line[index]
            if temp > result:
                result = temp
            temp = 1

print(result)