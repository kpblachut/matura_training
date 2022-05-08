data = []

with open('sygnaly.txt') as file:
    for line in file.readlines():
        line = line.removesuffix("\n")
        data.append(line)


result = [""]
highest_count = 0

for word in data:
    if len(set(word)) >= highest_count: # Finds the highest count of unique letters
        highest_count = len(set(word))
        
        if len(set(result[0])) < len(set(word)): # Checks if word has more unique letters then the result
            result = [word] # if it does, replaces all words with new word
            continue
        result.append(word) # Else appends the words

print(result[0])
print(len(set(result[0]))) # Prints number of unique letters