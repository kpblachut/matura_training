result = 0

with open("dane.txt", "r") as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split()

        # For every line in file checks if it's symetrical
        for j in range(160):
            if line[j] != line[-j - 1]: # Compares two symetrical item, if they are different result is incremented 
                result += 1
                break


print(result)