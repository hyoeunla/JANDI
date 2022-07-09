# 2xn 타일링
n = int(input())
nlist = [0 for _ in range(n)]
if n > 2:
    nlist[0] = 1
    nlist[1] = 2
    for i in range(2, n):
        nlist[i] = nlist[i-1]+nlist[i-2]
    print(nlist[n-1] % 10007)
else:
    print(n)
