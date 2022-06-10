data = []

with open("liczby2.txt", 'r') as file:
    for line in file.readlines():
        line = line.removesuffix('\n') # Removes newline suffix
        data.append(int(line)) # Converts string to integer value, then appends to the data array 

result = [data[0]]
lenght = 1
final_index = 0 # Holds the last index of the streak
for index, num in enumerate(data[1:-1]): # Cuts the first element out of for loop
    if result[len(result) - 1] <= num: # If the last element is <= num then add it to the array
        result.append(num)
        continue
    if len(result) > lenght: # Checks if current streak is longest than the last one 
        lenght = len(result)
        final_index = index 
    result = [num] # Resets the streak

result = data[final_index - lenght + 1: final_index + 1] # Based on lenght of the streak and it's last index crops the streak from the entire file

print(f'first number: {result[0]} | lenght: {len(result)}')