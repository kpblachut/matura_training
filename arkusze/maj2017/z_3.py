data = []

with open("dane.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split()

        line = [int(x) for x in line] # Converts all items to integers
        data.append(line)

heatmap = [[0 for i in range(320)] for i in range(200)] # Creates array full of zeros as a blank heatmap

for index, line in enumerate(data): 
    for i in range(len(line)- 1):
        if abs(line[i] - line[i+1]) > 128: # Checks if the differnce is higher than 128. If it is, adds two peaks to heatmap
            heatmap[index][i] = 1 
            heatmap[index][i+1] = 1

data = list(zip(*data)) # Replace rows with columns and columns with rows for data array
heatmap = list(zip(*heatmap)) # Replace rows with columns and columns with rows for heatmap array
heatmap = [list(x) for x in heatmap] # Converts rows from tuples to lists to enable editing
for index, line in enumerate(data):
    for i in range(len(line)- 1):
        if abs(line[i] - line[i+1]) > 128:
            heatmap[index][i] = 1
            heatmap[index][i+1] = 1

result = 0
# Counts peaks in heatmap
for i in heatmap:
    for j in i:
        if j > 0:
            result += 1

print(result)
