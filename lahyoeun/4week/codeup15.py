'''
[우리밋의 LAST 보너스 문제] 내 미래
해당 문제는 이차원 배열의 개념과 원리를 파악하기 위해 "우리밋"이 직접 만든 문제임을 알려드립니다. 
x축과 y축의 개념을 머릿 속에서 자유롭게 조작할 수 있도록 훈련하기 위해 만든 문제입니다.
이 점을 기억하시고 아래 문제를 푸시길 바랍니다.
해당 문제를 배포하시거나 외부에서 사용하실 때는 "우리밋"을 한번씩만 거론 부탁드리겠습니다.
구독만 해주신다면 그것으로 충분합니다.

ps. "내 미래"가 해당 문제 이름입니다. 참고로 전 다녀왔습니다. :)
훈련병인 철수는 교관의 지시에 따라야한다.
교관은 "좌로 1보, 하로 2보 가!"와 같이 좌,우,상,하로 이동할 것을 명령한다.
철수의 현재 위치가 입력으로 주어질 때 교관의 명령대로 이동한 위치는 어디일까?

제한 조건
1. 철수의 현재 위치는 첫 입력 값으로 공백을 두고 입력된다. 
  ex) 1 1 => (0, 0), 5 4 => (4, 3)
2. 훈련소의 전체 공간 크기는 5*5 이다.
3. 교관이 지시한 명령은 절대 훈련소 공간을 벗어나지 않는다.
4. 좌는 왼쪽, 우는 오른쪽, 상은 위쪽, 하는 아래쪽으로 한다.
5. 입력은 좌,우,상,하의 순서대로 공백을 두고 입력된다. 
  ex) 3 2 3 3 => 좌로 2보, 우로 2보, 상으로 3보, 하로 3보 이동.
입력

3 3
1 2 1 3
출력

0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 0
'''
cur = tuple(map(int, input().split()))
lf, rgt, up, down = map(int, input().split())
coords = [[0 for _ in range(5)] for _ in range(5)]

move = (cur[0] - up + down, cur[1] - lf + rgt)
coords[move[0] - 1][move[1] - 1] = 1

for crd in coords:
    print(*crd)

# 모르겠어서 강의 봄


'''
[96] 바둑판에 흰 돌 놓기
영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가 "바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

입력
바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
둘째 줄 부터 n+1 번째 줄까지 흰 돌을 놓을 좌표(x, y)가 n줄 입력된다.
n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 같은 좌표는 입력되지 않는다.

5
1 1
2 2
3 3
4 4
5 5
출력
흰 돌이 올려진 바둑판의 상황을 출력한다.
흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.

1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''
n = int(input())
baduk = [[0 for _ in range(19)] for _ in range(19)]

for _ in range(n):
    x, y = map(int, input().split())
    baduk[x-1][y-1] = 1

for bd in baduk:
    print(*bd)


'''
[97] 바둑판에 십자 뒤집기
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

입력
바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
2
10 10
12 12
출력
십자 뒤집기 결과를 출력한다.

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''
# 초기 십자 바둑판 입력
baduk = []
for _ in range(19):
    matrix = list(map(int, input().split()))
    baduk.append(matrix)

# n과 좌표 값을 입력받고 그에 따라 십자 형태에 맞춰 흑->백, 백->흑으로 변환
n = int(input())
for _ in range(n):  # n번 입력
    x, y = map(int, input().split())  # x와 y 좌표 입력
    for i in range(19):  # 변환
        baduk[i][y-1] = 1 if baduk[i][y-1] == 0 else 0  # 0->1, 1->0으로 변환
        baduk[x-1][i] = 1 if baduk[x-1][i] == 0 else 0  # 0->1, 1->0으로 변환

# 변환된 값을 한 줄 단위로 출력
for i in range(19):
    print(*baduk[i])


'''
[98] 설탕과자 뽑기
**서론**
부모님과 함께 유원지에 놀러간 영일이는
설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,
막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.  
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)
대체 텍스트

격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

입력
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

[입력값의 정의역]
1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

5 5
3
2 0 1 1
3 1 2 3
4 1 2 5
출력
모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.

1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
'''
h, w = map(int, input().split())
shape = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())

for _ in range(n):
    l, d, x, y = map(int, input().split())
    x, y = x-1, y-1

    if d == 0:
        for i in range(l):
            shape[x][y+i] = 1
    else:
        for i in range(l):
            shape[x+i][y] = 1

for s in shape:
    print(*s)


'''
[99] 성실한 개미
**서론**
영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.

왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데,
그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.
미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는 더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며, 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

입력
10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.

1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
출력
성실한 개미가 이동한 경로를 9로 표시해 출력한다.

1 1 1 1 1 1 1 1 1 1
1 9 9 1 0 0 0 0 0 1
1 0 9 1 1 1 0 0 0 1
1 0 9 9 9 9 9 1 0 1
1 0 0 0 0 0 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
ant_house = []
for i in range(5):
    matrix = list(map(int, input().split()))
    ant_house.append(matrix)

print('===================')

x, y = 1, 1
while ant_house[x][y] != 2:
    if ant_house[x][y] == 0:
        ant_house[x][y] = 9
        y += 1
    else:
        x += 1
        y -= 1
ant_house[x][y] = 9

for house in ant_house:
    print(*house)
