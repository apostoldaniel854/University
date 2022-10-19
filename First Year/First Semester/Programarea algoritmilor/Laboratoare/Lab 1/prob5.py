n = int(input("n="))
k = 0
while n > 0:
    k += 1
    n = n & (n - 1)
print("Numarul are", k, "biti de 1")
