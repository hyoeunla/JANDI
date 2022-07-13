# 바닥 공사

n = int(input())
if n > 2:
    nlist = [0 for _ in range(n+1)]
    nlist[1] = 1
    nlist[2] = 3
    for i in range(3, n+1):
        nlist[i] = nlist[i-1]+nlist[i-2]*2
    print(nlist[n] % 796796)
else:
    print(n % 796796)
