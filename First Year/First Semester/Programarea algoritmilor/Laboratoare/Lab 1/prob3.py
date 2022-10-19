n = int(input("n="))
a = list(map(int, input().split()))
xr = 0
for x in a:
    xr ^= x
print("Valoarea care apare o singura data este", xr)
