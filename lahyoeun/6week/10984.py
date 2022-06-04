t = int(input(""))
for i in range(t):
    n = int(input(""))
    a = 0
    b = 0

    for j in range(n):
        H, G = input("").split()
        H, G = int(H), float(G)
        a += H
        b += (H*G)
    b /= a
    print(a, round(b, 1))
