n = int(input("n="))
for mask in range((1 << n)):
    subset = []
    for i in range(n):
        if ((1 << i) & mask) > 0:
            subset.append(i + 1)
    print(subset)
