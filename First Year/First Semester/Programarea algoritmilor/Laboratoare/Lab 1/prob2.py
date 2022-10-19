x = int(input("x="))
if (x & (x - 1)) == 0:
    k = 0
    while (1 << k) < x:
        k += 1
    print("Numarul este de forma 2 8^", k)
else:
    print("Numarul nu este de forma 2^k")
