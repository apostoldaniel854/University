n = int(input("n="))
curs = list(map(float, input().split()))
maxChange = 0
changeDay = 0
for i in range(n - 1):
    if curs[i + 1] - curs[i] > maxChange:
        maxChange = curs[i + 1] - curs[i]
        changeDay = i + 1
print("Intre zilele", changeDay, "si", changeDay + 1, "a avut loc cea mai mare crestere a cursului valutar egala cu", maxChange)
