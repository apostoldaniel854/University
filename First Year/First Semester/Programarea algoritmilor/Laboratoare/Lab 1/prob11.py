import math

def prim(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

a = int(input("a="))
b = int(input("b="))
ans = -1
for x in range(a, b + 1):
    if prim(x) == True:
        print(f"Primul numar prim din [{a}, {b}] este", x)
        break
else:
    print(f"Nu exista niciun numar prin in [{a}, {b}]")
