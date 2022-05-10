data = []

with open("liczby.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix("\n")
        data.append(line)

result = []

for num in data:
    sum = 0

    # Calcualtes the sum of factorials of digits
    for n in num:
        factorial = 1
        for i in range(int(n)):
            factorial *= i + 1
        sum += factorial

    if sum == int(num):
        result.append(sum)

print(*result, sep="\n") # Prints all items in seperate lines