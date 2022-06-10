def nwd(a, b):
    while b != 0:
        result = a % b
        a = b
        b = result
    return a

nums = [36, 24, 72, 150]

result = nwd(nums[0], nums[1])
for i in range(2, len(nums)):
    result = nwd(result, nums[i])
    
print(result)
