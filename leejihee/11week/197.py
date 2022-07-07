# 2. 부품찾기
# 나의 풀이 - 집합 자료형 이용 방법
n = int(input())
stock = list(map(int, input().split()))
m = int(input())
need = list(map(int, input().split()))

for i in range(m):
    if need[i] in stock:
        print('yes', end=' ')
    else:
        print('no', end=' ')
