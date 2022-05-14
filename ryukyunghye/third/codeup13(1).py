# 13. 기초 - 종합(1)

# [78] 짝수 합 구하기
num = int(input())
sum1 = 0
for i in range(0, num+1, 2):
    sum1 += i
print(sum)
# 다른 방법들
sum2 = [i for i in range(2, num+1, 2)]
print(sum(sum2))
sum3 = range(2, num+1, 2)
print(sum(sum3))

# [79] 원하는 문자가 입력될 때까지 반복 출력하기
# while문
char = input().split()
while char != 'q':
    print(char[i])
    i += 1
# for문
char = input().split()
for i in char:
    if i == 'q':
        break
    print(i)

# [80] 언제까지 더해야 할까?
# while문
num = int(input())
sum, i = 0
while sum < num:
    i += 1
    sum += i
print(i)
# for문
num = int(input())
sum = 0
for i in range(1, num+1):
    sum += i
    if (sum >= num):
        break
    print(i)  # i 출력은 break위에도 괜찮음

# [81] 주사위를 2개 던지면?
n, m = int(input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

# [82] 16진수 구구단
num = int(input())
for i in range(1, 16):
    print('{}*{}={}'.format(num, hex(i)[2:].upper, hex(int, num, 16)*i[2:]))

# [83] 3 6 9 게임의 왕이 되자
num = int(input())
for i in range(1, num+1):
    if i % 3 == 0:
        print('x', end=' ')
    print(i, end=' ')

# [84] 빛 섞어 색 만들기
r, g, b = map(int, input().split())
sum = 0
for x in range(r):
    for y in range(g):
        for z in range(b):
            print(x, y, z)
            sum += 1
print(sum)

# [85] 소리 파일 저장용량 계산하기
h, b, c, s = map(int, input().split())
result = (h*b*c*s)/(8*1024**2)
print(round(result, 1), 'MB')
