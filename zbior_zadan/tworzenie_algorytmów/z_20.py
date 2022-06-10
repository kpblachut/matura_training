x = 3190
b = 7

fin = x
num = []
while x > 0:
    num.append(x % b)
    x //= b

sum = 0
for i in range(len(num)):
    temp = 1
    for j in range(len(num)):
        temp *= num[i]

    sum += temp

print(sum)

if sum == fin:
    print("TAK")
else:
    print("NIE")