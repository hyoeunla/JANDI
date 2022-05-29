from unittest import result


n, m = map(int, input().split())
weight = list(map(int, input().split()))

array = [0] * 11

for i in weight:
    array[i] += 1

dap = 0

for i in range(1, m+1):
    n -= array[i]
    dap += array[i] * n

print(dap)
