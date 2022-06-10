instructions = []

with open('przyklad.txt') as file:
    for line in file.readlines():
        line = line.removesuffix('\n')
        line = line.split(" ")
        instructions.append(line)


def checkLenght(instructions):
    count = 0
    for instruction, letter in instructions:
        if instruction == "DOPISZ":
            count += 1
        elif instruction == "USUN":
            count -= 1
        
    return count

def findLongestOccurence(instructions):
    count = 1
    longestOccurence = ""
    lastInstruction = instructions[0][0]
    tempCount = 1

    for instruction, letter in instructions:
        if instruction == lastInstruction:
            tempCount += 1

            if tempCount > count:
                count = tempCount
                longestOccurence = instruction
        else:
            tempCount = 1
        
        lastInstruction = instruction

    return count, longestOccurence

def encode(instructions):
    text = []

    for instruction, letter in instructions:
        if instruction == "DOPISZ":
            text.append(letter)
        elif instruction == "USUN":
            text.pop(len(text) - 1)
        elif instruction == "ZMIEN":
            text[len(text) - 1] = letter
        elif instruction == "PRZESUN":
            for i, l in enumerate(text):
                if l == letter:
                    if l == "Z":
                        letter = "A"
                    else:
                        letter = chr(ord(letter) + 1)
                    text[i] = letter
                    break

    print("".join(text))




print(findLongestOccurence(instructions))
encode(instructions)

