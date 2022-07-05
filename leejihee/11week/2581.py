# 2581. 소수
m = int(input())
n = int(input())
list = []

for i in range(m, n+1):
    for j in range(2, i):
        if i % j == 0:  # 한번이라도 걸리면 소수가 아님
            break
    else:
        list.append(i)

if 1 in list:
    list.remove(1)

if not list:
    print(-1)
else:
    print(sum(list))
    print(list[0])
