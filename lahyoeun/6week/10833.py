count = int(input())
N = 0
for i in range(count):
    a, b = map(int, input().split())
    c = b % a
    N = N + c
print(N)
