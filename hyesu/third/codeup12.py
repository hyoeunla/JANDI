'''
[71]
정수가 순서대로 입력된다.
(단, 개수는 알 수 없다.)

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
while( ), for( ) 등의 반복문을 사용할 수 없다.
'''


def goto(array, i):
    if array[i] == 0:
        return
    print(array[i])
    i += 1
    goto(array, i)


array = list(map(int, input().split()))
goto(array, i=0)

'''
[72]

n개의 정수가 순서대로 입력된다.
(단 n의 최대 개수는 알 수 없다.)

n개의 입력된 정수를 순서대로 출력해보자.
while( ), for( ) 등의 반복문을 사용할 수 없다.
'''
n = int(input())
num = list(map(int, input().split()))

print('== #1 ==')


def goto(num, n, i):
    if i == n:
        return
    print(num[i])
    i += 1
    goto(num, n, i)

    goto(num, n, 0)


'''
[73]

정수가 순서대로 입력된다.
(단, 개수는 알 수 없다.)

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
'''
number = map(int, input().split())

for i in number:
    if i == 0:
        break
    print(i)

'''
[74]

정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
'''
n = int(input())

for i in range(n, 0, -1):
    print(i)


'''
[75]

정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
'''
n = int(input())

for i in range(n-1, -1, -1):
    print(i)


'''
[76]

영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.
'''
n = input()

for i in range(ord('a'), ord(n) + 1):
    print(chr(i), end=' ')


'''
[77]

정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
'''
n = int(input())

for i in range(n + 1):
    print(i)
