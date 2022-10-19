def rev(n):
    ans = 0
    while n > 0:
        ans = ans * 10 + n % 10
        n = n // 10
    return ans

n = int(input("n="))
if n == rev(n):
    print(n, "este palindrom")
else:
    print(n, "NU este palindrom")
