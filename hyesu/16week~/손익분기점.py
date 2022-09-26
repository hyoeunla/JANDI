# 손익분기점

a, b, c = map(int, input().split())
num = 0

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)
