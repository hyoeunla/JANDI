# 사과

S = int(input())
num = 0
for i in range(S):
    A, B = map(int, input().split())
    num += B % A

print(num)
