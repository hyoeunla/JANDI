# 2. 위에서 아래로
n = int(input())
list = []

for i in range(n):
    list.append(int(input()))
list.sort(reverse=True)
print(*list)  # for문을 사용해서 하나씩 출력할 수도 있음
