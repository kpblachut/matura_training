data = []

with open("liczby2.txt", 'r') as file:
    for line in file.readlines():
        line = line.removesuffix('\n') # Removes newline suffix
        data.append(line) # Converts string to base10 from base8 value, then appends to the data array 

data_oct = [str(oct(int(x))) for x in data] # Converts items for str -> int -> oct -> str 

count_base10 = 0
count_base8 = 0

for i in range(len(data)):
    count_base10 += data[i].count("6")
    count_base8 += data_oct[i].count("6")

print(f"6's in base10: {count_base10} | 6's in base8: {count_base8}")