# 13. 기초 - 종합(2)

# [86] 그림 파일 저장용량 계산하기
w, h, b = map(int, input().split())
result = (w*h*b)/(8*1024**2)
print(round(result, 2), 'MB')

# [87] 여기까지! 이제 그만~
# for
num = int(input())
sum = 0
for i in range(1, num+1):
    if sum >= num:
        break
    sum += i
    i += 1
print(sum)

# while
num = int(input())
sum = 0
i = 0
while sum < num:
    sum += i
    i += 1
print(sum)


# [88] 3의 배수는 통과?
num = int(input())
for i in range(1, num+1):
    if i % 3 != 0:
        print(i, end=' ')

# [89] 수 나열하기1
a, d, n = map(int, input().split())
count = 0
turn = []
while count < n:
    turn.append(a)
    a += d
    count += 1
print(turn[-1])


# [90] 수 나열하기2
a, r, n = map(int, input().split())
count = 0
turn = []
while count < n:
    turn.append(a)
    a *= r
    count += 1
print(turn[-1])

# [91] 수 나열하기3
a, m, d, n = map(int, input().split())
count = 0
turn = []
while count < n:
    turn.append(a)
    a = a*m+d
    count += 1
print(turn[-1])

# [92] 함께 문제 푸는 날
# while문
a, b, c = map(int, input().split())
day = 1
while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)
# +if문
a, b, c = map(int, input().split())
day = 1
while True:
    day += 1
    if day % a == 0 and day % b == 0 and day % c == 0:
        break
print(day)
