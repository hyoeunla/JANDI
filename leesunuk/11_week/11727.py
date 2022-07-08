# 2xn 타일링 2
n = int(input())
if n > 1:
    nlist = [0 for _ in range(n)]
    nlist[0] = 1
    nlist[1] = 3
    for i in range(2, n):
        nlist[i] = nlist[i-1]+nlist[i-2]*2
    print(nlist[n-1] % 10007)
else:
    print(n)
