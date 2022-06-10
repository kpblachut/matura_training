k = 5
y = 11
x = 12

def check(k , y, x):
    result = k
    cp = pow(2,k) / 2

    while result > 1:
        if x >= cp and y >= cp:
            cp += cp/2
            print(cp)
            result -= 1
            continue
        if x < cp and y < cp:
            cp = cp/2
            result -= 1
            continue
        return result
    return result

print(check(k, y, x))