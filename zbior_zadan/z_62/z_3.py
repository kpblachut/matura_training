data1 = []
data2 = []

with open("liczby1.txt", 'r') as file:
    for line in file.readlines():
        line = line.removesuffix('\n') # Removes newline suffix
        data1.append(int(line, 8)) # Converts string to base10 from base8 value, then appends to the data array 

with open("liczby2.txt", 'r') as file:
    for line in file.readlines():
        line = line.removesuffix('\n') # Removes newline suffix
        data2.append(int(line)) # Converts string to integer value, then appends to the data array 

count_a = 0 # Counts when the elemntes of correspondent indexes from both arrays are the same
count_b = 0 # Counts when the element from data1 is greater then element of correspondent index from data2 

for i in range(len(data1)):
    if data1[i] == data2[i]:
        count_a += 1
        continue
    if data1[i] > data2[i]:
        count_b += 1

print(f"a) {count_a} | b) {count_b}")