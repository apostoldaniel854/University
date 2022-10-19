n = int(input("n="))
a = list(map(int, input().split()))
maxValue = a[0]
minValue = a[0]
for i in range(1, n):
    if (maxValue < a[i]):
        maxValue = a[i]
    elif (minValue > a[i]):
        minValue = a[i]
print(minValue, maxValue)
