ll1 = int(input("l1="))
ll2 = int(input("l2="))
a = ll1
b = ll2
while b > 0:
    r = a % b
    a = b
    b = r
print("Mesterul are nevoie de de", ll1 * ll2 // (a * a), "de latura", a)
