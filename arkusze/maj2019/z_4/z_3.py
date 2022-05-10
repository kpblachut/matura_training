from math import gcd # Greatest common divisor

data = []

with open("liczby.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix("\n")
        data.append(int(line))


streak = [data[0], data[1]] 
highest_count = 2 # Keeps track of the longest streak
runner_up = 2 # Keeps track of the current streak
final_nwd = 1 # GCD of the longest streak
starter = 1 # First number of the longest streak

for index in range(2, len(data)):
    nwd = gcd(*streak) # Calculates the GDC for the entire streak
    if gcd(nwd, data[index]) > 1: # Checks if the current number and rest of the numbers in streak have common GCD greater than 1
        streak.append(data[index])
        runner_up += 1

        if runner_up > highest_count:
            highest_count = runner_up
            starter = streak[0]
            final_nwd = nwd
        continue
    streak = [data[index - 1], data[index]] # Resets the streak if the GDC is equal to 1
    runner_up = 2

# Printing results
print(highest_count)
print(starter)
print(final_nwd)