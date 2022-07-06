# 부품찾기
n = int(input())
array = list(map(int, input().split()))
m = int(input())
marray = list(map(int, input().split()))
array = sorted(array)

for i in marray:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
