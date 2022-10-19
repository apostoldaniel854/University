x = int(input("x="))
n = int(input("n="))
x = ((x & ((1 << (n - 1)) - 1)) | ((x >> n) << (n - 1)))
print("Numarul determinat prin stergerea bitului", n, "este", x)
