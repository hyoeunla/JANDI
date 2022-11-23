# 10828 스택
n = int(input())

stack = []
for i in range(n):
    x = input()
    if x == 'top':
        if stack > 0:
            