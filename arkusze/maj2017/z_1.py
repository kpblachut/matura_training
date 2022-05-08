data = []

with open("dane.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split()

        for c in line:
            data.append(int(c))


print(max(data)) # Finds the largest item in the list
print(min(data)) # Finds the lowest item in the list