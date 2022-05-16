'''
71번: 정수가 순서대로 입력된다.
(단, 개수는 알 수 없다.)

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
while( ), for( ) 등의 반복문을 사용할 수 없다.

입력
정수가 순서대로 입력된다.
7 4 2 3 0 1 5 6 9 10 8

입력된 정수를 줄을 바꿔 하나씩 출력하는데, 0이 입력되면 종료한다. (0은 출력하지 않는다.)
7
4
2
3
'''


def IP(a, b):
    if a[b] == 0:
        return
    else:
        print(a[b])
        b = b+1
        IP(a, b)


a = list(map(int, input("원하는 숫자들을 입력해주세요: ").split()))
IP(a, b=0)

'''
72번: n개의 정수가 순서대로 입력된다.
(단 n의 최대 개수는 알 수 없다.)

n개의 입력된 정수를 순서대로 출력해보자.
while( ), for( ) 등의 반복문을 사용할 수 없다.

입력
첫 줄에 정수의 개수 n이 입력되고, 두 번째 줄에 n개의 정수가 공백을 두고 입력된다.
'''


def PT(a, b):
    if len(a) < b+1:
        return
    else:
        print(a[b])
        b = b+1
        PT(a, b)


c = input("입력하실 숫자의 개수를 입력해주세요: ")
a = list(map(int, input("원하는 숫자들을 입력해주세요: ").split()))

PT(a, b=0)

'''
다른 방법
'''
n = int(input())
number = list(map(int, input().split()))

print('== #1 ==')


def goto(number, n, i):
    if i == n:
        return
    print(number[i])
    i += 1
    goto(number, n, i)


goto(number, n, 0)

'''
차이점: 나는 따로 받은 C를 활용하지 않고 문제를 풀었고, 다른 방법에선 input으로 받은 number와 n을 모두 활용해주었다
'''

'''
73번: 정수가 순서대로 입력된다.
(단, 개수는 알 수 없다.)

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
'''
a = list(map(int, input("원하는 정수들을 입력해주세요: ").split()))
for i in a:
    if i == 0:
        break
    else:
        print(a[i-1])

'''
74번: 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

출력
1씩 줄이면서 한 줄에 하나씩 1이 될 때까지 출력한다.
'''


def PT(a):
    for i in range(a, 0, -1):
        print(i)


a = int(input("1~100까지의 수 중 하나를 입력해주세요: "))
PT(a)

'''
75번:정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

출력
1씩 줄이면서 한 줄에 하나씩 0이 될 때까지 출력한다.

4
3
2
1
0
'''


def PT(a):
    for i in range(a-1, -1, -1):
        print(i)


a = int(input("1~100까지의 수 중 하나를 입력해주세요: "))
PT(a)

'''
76번: 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

입력
영문자 1개가 입력된다. (a ~ z)

f

출력
a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.

a b c d e f
'''


def PT(a):
    for i in range(97, a+1, 1):
        print(chr(i))


a = input("영문자 한개a ~ z)를 입력해주세요: ")
b = ord(a)
PT(b)

'''
77번: 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

입력
정수 1개가 입력된다. (0 ~ 100)

4

출력
0부터 그 수까지 줄을 바꿔 한 개씩 출력한다.

0
1
2
3
4
'''


def PT(a):
    for i in range(0, a+1):
        print(i)


a = int(input("정수 1개를 입력해주세요: "))
PT(a)
