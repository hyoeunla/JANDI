# 더하기
n = int(input())
for i in range(n):
    result = 0
    sn = int(input())
    array = map(int, input().split())
    for j in array:
        result += j
    print(result)
