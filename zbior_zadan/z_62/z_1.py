data = []

with open("liczby1.txt", 'r') as file:
    for line in file.readlines():
        line = line.removesuffix('\n') # Removes newline suffix
        data.append(line) 


print(f"min val: {min(data)}, max val: {max(data)}") # Prints out minimum and maximum value of data array