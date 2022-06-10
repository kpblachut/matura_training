data = []

with open("liczby.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        data.append(line)


result = []
for num in data:
    if int(num) < 1000:
        result.append(num)

print(f"Liczby mniejsze od 1000: {len(result)} | Dwie ostatnie liczby: {result[-2]}, {result[-1]}")