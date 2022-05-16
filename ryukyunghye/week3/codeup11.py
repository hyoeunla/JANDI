#  11. 기초 - 조건/선택실행구조

# [65] 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
a, b, c = map(int, input().split())
# 방법1
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if not c % 2:
    print(c)
# 방법2
# filter(Function, Iterable) : 참인 것들만 걸러서 반환
a, b, c = map(int, input().split())
print(*(filter(lambda num: num % 2 == 0, [a, b, c])))

# [66] 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
# 방법1
a, b, c = map(int, input().split())
print(a % 2 and 'odd' or 'even')
print('odd' if b % 2 else 'even')
print(['even', 'odd'][c % 2])
# 방법2
a, b, c = map(int, input().split())
print(*map(lambda num: 'odd' if num % 2 else 'even', [a, b, c]))

# [67] 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
# 방법1
num = int(input())
print('plus' if num > 0 else 'minus')
print('even' if num % 2 == 0 else 'odd')
# 방법2
num = int(input())
print(num > 0 and 'plus' or 'minus')
print(num % 2 and 'odd' or 'even')

# [68] 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
score = int(input())
if 90 <= score <= 100:
    print('A')  # if score >=90도 가능함
elif 70 <= score <= 89:
    print('B')
elif 40 <= score <= 69:
    print('C')
else:
    print('D')


# [69] 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
char = input()
if char == 'A':
    print('best!!!')
elif char == 'B':
    print('good!!')
elif char == 'C':
    print('run!')
elif char == 'D':
    print('slowly~')
else:
    print('what?')

# [70] 월이 입력될 때 계절 이름이 출력되도록 해보자.
month = int(input())
if (month == 12 or month == 1 or month == 1):
    print('winter')
elif(month == 3 or month == 4 or month == 5):
    print('spring')
elif(month == 6 or month == 7 or month == 8):
    print('summer')
else:
    print('fall')
