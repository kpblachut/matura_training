a = [2,2,1,3]
b = [1,2,0,0]
p = 4
n = 4 

c = []
reszta = 0
for i in range(n):
    result = a[i] + b[i] + reszta
    if result < p:
        reszta = 0
        c.append(result)
    else:
        reszta = result // p
        result %= p
        c.append(result)

while reszta != 0:
    result = reszta % p
    reszta //= p
    c.append(result)

while len(c) < n+1:
    c.append(0)

print(c)