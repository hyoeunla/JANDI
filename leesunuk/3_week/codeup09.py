'''
59번: 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.

예를 들어 1이 입력되었을 때 저장되는
1을 32비트 2진수로 표현하면 00000000 00000000 00000000 00000001 이고,
~1은 11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미한다.
'''

a = int(input("정수 1개를 입력해주세요: "))
print(~a)

'''
60번: 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3 : 00000000 00000000 00000000 00000011
5 : 00000000 00000000 00000000 00000101
3 & 5 : 00000000 00000000 00000000 00000001
이 된다.
'''
a, b = map(int, input("정수 2개를 입력해주세요: ").split())
print(a & b)


# 우리밋이 알려주는 Bonus 문제(2)
'''
1개의 정수형 입력이 들어오면 비트 연산을 이용하여 '홀수'와 '짝수'를 판별하여라

Tip::

'짝수'와 '홀수'를 리스트에 담고 짝수일 때는 '짝수'를, 홀수일 때는 '홀수'를 출력하게 한다.
0이 아닌 어떠한 정수일지라도 1과 비트단위 논리곱(&)을 수행하게 되면 1이 되는 특성을 이용한다.
'''
PB = {1: "홀수", 0: "짝수"}
a = int(input("정수 1개를 입력해주세요: "))
if a & 1 == 1:
    print(PB[1])
else:
    print(PB[0])

'''
61번: 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3 : 00000000 00000000 00000000 00000011
5 : 00000000 00000000 00000000 00000101
3 | 5 : 00000000 00000000 00000000 00000111
'''

a, b = map(int, input("정수 2개를 입력해주세요: ").split())
print(a | b)


'''
62번:입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3 : 00000000 00000000 00000000 00000011
5 : 00000000 00000000 00000000 00000101
3 ^ 5 : 00000000 00000000 00000000 00000110
이 된다.
'''
a, b = map(int, input("정수 2개를 입력해주세요: ").split())
print(a ^ b)


# 우리밋이 알려주는 Bonus문제(2-2)
'''
직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다. 
점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요.

단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.

제한사항

v는 세 점의 좌표가 들어있는 2차원 배열입니다.
v의 각 원소는 점의 좌표를 나타내며, 좌표는 [x축 좌표, y축 좌표] 순으로 주어집니다.
좌표 값은 1 이상 10억 이하의 자연수입니다.
직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 [x축 좌표, y축 좌표] 순으로 담아 return 해주세요.

입력(1)

[[1,4], [3,4], [3,10]]

출력(1)

[1,10]

입력(2)

[[1,1], [2,2], [1,2]]

출력(2)

[2,1]
'''

a = [[1, 4], [3, 4], [3, 10]]
b = []
for i in range(2):
    if a[0][i] == a[1][i]:
        b.append(a[2][i])
    elif a[1][i] == a[2][i]:
        b.append(a[0][i])
    else:
        b.append(a[1][i])
print(b)
