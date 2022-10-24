# 개수 세기

n = int(input())
nlist = map(int, input().split())
v = int(input())

count = 0
for i in nlist:
    if i == v:
        count += 1

print(count)
