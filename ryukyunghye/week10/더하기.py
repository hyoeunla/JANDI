# [9085] 더하기
# 방법1
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    print(sum(numbers))

# 방법2 -> sum의 위치 차이
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = sum(list(map(int, input().split())))
    print(numbers)
