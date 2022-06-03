# [10833] 사과
N = int(input())
result = 0
for _ in range(N):
    s, a = map(int,input().split())
    result = a%s + result
print(result)