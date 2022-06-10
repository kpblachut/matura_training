data = []

with open('liczby.txt', 'r') as file:
    for line in file.readlines():
        if int(line.strip()) % 2 != 0:
            data.append(int(line.strip()))

print(len(data))

# all_factors = []
# for n in data:
#     num = n
#     factors = []
#     k = 2
#     is_even = False
#     while num != 1 and not is_even:
#         while num % k == 0:
#             num //= k
#             factors.append(k)
#             if k == 2:
#                 is_even = True
#         k += 1
#     all_factors.append(factors)


# print(all_factors)