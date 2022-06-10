data = []

with open('galerie_przyklad.txt', 'r') as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split(" ")
        line_data = [line[0], line[1]]
        shops = []
        for i in range(2, len(line), 2):
            x = int(line[i])
            y = int(line[i+1])
            if line[i] != '0' :
                if x > y:
                    shops.append(f"{x}x{y}")
                if y > x:
                    shops.append(f"{y}x{x}")

        line_data.append(shops)
        data.append(line_data)

result = []

for country, city, shops in data:
    used = set()
    count = 1
    for shop in shops:
        # print(shop)
        # print(used)
        if shop not in used:
            count += 1
            used.add(shop)
        # print(count)
    result.append([city, len(used)])

print(result)
