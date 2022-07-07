# 2581. 소수
# 나의 풀이
m = int(input())
n = int(input())
list = []

for i in range(m, n+1):
    for j in range(2, i):
        if i % j == 0:  # 한번이라도 걸리면 소수가 아님
            break
    else:
        list.append(i)

if 1 in list:  # 1 제외하기
    list.remove(1)

if not list:
    print(-1)
else:
    print(sum(list))
    print(list[0])

# 다른 풀이
m = int(input())
n = int(input())
list = []

for i in range(m, n+1):
    if i != 1:  # 1 제외하기
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:  # check에 True/False를 줘서 판단하게 함!!
            list.append(i)
if not list:
    print(-1)
else:
    print(sum(list))
    print(list[0])
