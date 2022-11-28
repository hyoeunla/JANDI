# 2750번: 수 정렬하기

n = int(input())
nlist = [0 for _ in range(n)]
for i in range(n):
    nlist[i] = int(input())

nlist.sort()
for i in range(n):
    print(nlist[i])
