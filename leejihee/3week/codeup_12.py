'''
[71]
정수가 순서대로 입력된다.
(단, 개수는 알 수 없다.)

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
while( ), for( ) 등의 반복문을 사용할 수 없다.

입력
정수가 순서대로 입력된다.
7 4 2 3 0 1 5 6 9 10 8

출력
입력된 정수를 줄을 바꿔 하나씩 출력하는데, 0이 입력되면 종료한다. (0은 출력하지 않는다.)
7
4
2
3
'''


def goto(array, i):   # 함수 정의, 매개변수 설정
    if array[i] == 0:  # 0일 때 멈추기
        return
    print(array[i])
    i += 1            # 방 번호 추가
    goto(array, i)


array = list(map(int, input().split()))
goto(array, i=0)

'''
[72]
n개의 정수가 순서대로 입력된다.
(단 n의 최대 개수는 알 수 없다.)

n개의 입력된 정수를 순서대로 출력해보자.
while( ), for( ) 등의 반복문을 사용할 수 없다.

입력
첫 줄에 정수의 개수 n이 입력되고, 두 번째 줄에 n개의 정수가 공백을 두고 입력된다.
5  
1 2 3 4 5  

출력
n개의 정수를 한 개씩 줄을 바꿔 출력한다.
1  
2  
3  
4  
5  
'''
count = int(input())
num = list(map(int, input().split()))
for i in range(count):
    print(num[i])

# count = int(input())
# num = list(map(int, input().split()))
# for i in range(count, 0, -1):
#     print(num[i-1])

'''
[73]
정수가 순서대로 입력된다.
(단, 개수는 알 수 없다.)

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

입력
정수가 순서대로 입력된다.
7 4 2 3 0 1 5 6 9 10 8

출력
입력된 정수를 줄을 바꿔 하나씩 출력하는데, 0이 입력되면 종료한다. (0은 출력하지 않는다.)
7
4
2
3
'''
# 71번을 for문을 사용해서 풀기
num = map(int, input().split())
for i in num:
    if i == 0:
        break
    print(i)

'''
[74]
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

입력
정수 1개가 입력된다. (1 ~ 100)
5

출력
1씩 줄이면서 한 줄에 하나씩 1이 될 때까지 출력한다.
5
4
3
2
1
'''
# 나의 풀이
num = int(input())
for i in range(num):
    print(num-i)

# 해설
count = int(input())
for i in range(count, 0, -1):
    print(i)

'''
[75]
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

입력
정수 1개가 입력된다. (1 ~ 100)
5

출력
1씩 줄이면서 한 줄에 하나씩 1이 될 때까지 출력한다.
4
3
2
1
0
'''
count = int(input())
for i in range(count, 0, -1):
    print(i-1)

'''
[76]
영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

입력
영문자 1개가 입력된다. (a ~ z)
f

출력
a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.
a b c d e f
'''
c = ord(input())
for i in range(97, c+1):
    print(chr(i), end=" ")

'''
[77]
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

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
num = int(input())
for i in range(0, num+1):
    print(i)
