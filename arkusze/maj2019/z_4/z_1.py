data = []

with open("liczby.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix("\n")
        data.append(int(line))

result = []
# For every iteration devide num by consecutive powers of three whlie num is smaller or equal base (power of three)
for num in data:
    base = 1
    while num >= base:
        if num == base: # If num is equal base append num to to result array
            result.append(num)
        base *= 3

print(len(result))