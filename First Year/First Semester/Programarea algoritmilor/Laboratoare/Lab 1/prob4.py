x = int(input("x="))
n = int(input("n="))
x = ((x & ((1 << n) - 1)) | ((x >> (n + 1)) << n))
print("Numarul determinat prin stergerea bitului", n, "este", x)
