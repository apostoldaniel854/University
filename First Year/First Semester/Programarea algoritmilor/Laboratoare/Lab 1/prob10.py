import math
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
delta = b * b - 4 * a * c
if delta < 0:
    print("Nu exista radacini reale")
elif delta == 0:
    print("Exista o radacina dubla egala cu", -b / (2*a))
else:
    print("Exista doua radacini egale cu", - b + math.sqrt(delta) / (2 * a), "si", - b + math.sqrt(delta) / (2 * a))
