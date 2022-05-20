'''
[97] 바둑판에 십자 뒤집기
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...
"십(+)자 뒤집기를 해볼까?"하고 생각했다.
바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때, n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

입력
바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

출력
십자 뒤집기 결과를 출력한다.
'''
# 나의 풀이
brd = [[0 for _ in range(19)]for _ in range(19)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    for j in range(19):
        if brd[j][y] == 0:
            brd[j][y] = 1
        elif brd[j][y] == 1:
            brd[j][y] = 0

        if brd[x][j] == 0:
            brd[x][j] = 1
        elif brd[x][j] == 1:
            brd[x][j] = 0

for k in brd:
    print(*k)

# 해설
baduk = []
for _ in range(19):
    matrix = list(map(int, input().split()))
    baduk.append(matrix)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        brd[j][y] = 1 if brd[j][y] == 0 else 0
        brd[x][j] = 1 if brd[x][j] == 0 else 0

for k in brd:
    print(*k)
