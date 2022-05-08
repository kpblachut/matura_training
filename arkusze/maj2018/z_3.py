data = []

with open('sygnaly.txt') as file:
    for line in file.readlines():
        line = line.removesuffix("\n")
        data.append(line)

result = []

for word in data: 
    passed = True # Validator - default true
    for i in word:
        for j in word:
            if abs(ord(i) - ord(j)) > 10: # Checks if distance between two letters is greater then 10
                passed = False # If it is, changes validator to false
    
    if passed:
        result.append(word)

print(*result, sep='\n') # Prints every row of array in seperate line

with open("wynik.txt", "w") as file: # writes result to file
    for line in result:
        file.write(line + "\n")