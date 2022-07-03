# 부품 찾기
n = int(input())
N = list(map(int, input().split()))
arr = [0]*1000001
for i in N:
    arr[i] = 1
m = int(input())
M = list(map(int, input().split()))
for i in M:
    if arr[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')
