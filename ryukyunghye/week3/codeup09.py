# 9. 기초 - 비트단위 논리 연산
# [59] 입력된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자
bool = int(input())
print(~bool)

# [60] 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
a, b = map(int, input().split())
print(a & b)

# [우리밋이 알려주는 Bonus 문제(2)] 1개의 정수형 입력이 들어오면 비트 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
num = int(input())
print(["짝수", "홀수"][num & 1])

# [61] 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
a, b = map(int, input().split())
print(a | b)

# [62] 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
a, b = map(int, input().split())
print(a ^ b)


# [우리밋이 알려주는 Bonus 문제(2-2)]
# 방법1
dot = [[1, 4], [3, 4], [3, 10]]
result = []
for i in range(2):
    if dot[0][i] == dot[1][i]:
        result.append(dot[2][i])
    elif dot[0][i] == dot[2][i]:
        result.append(dot[1][i])
    elif dot[1][i] == dot[2][i]:
        result.append(dot[0][i])
print(result)

# 방법2
dot = [[1, 4], [3, 4], [3, 10]]
result = []
result.append(dot[0][0] ^ dot[1][0] ^ dot[2][0])
result.append(dot[0][0] ^ dot[1][1] ^ dot[2][1])
print(result)
