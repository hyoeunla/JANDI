M = int(input())
N = int(input())
gop = []
for i in range(M, N+1):
    j = i**(1/2)
    if j % 1 == 0:
        gop.append(int(j**2))
if len(gop) >= 1:
    print(sum(gop))
    print(gop[0])
else:
    print(-1)
