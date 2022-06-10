x = 575

p = x//2
while p**2 > x:
    print(p)
    p = (p+(x//p))//2

print(p)