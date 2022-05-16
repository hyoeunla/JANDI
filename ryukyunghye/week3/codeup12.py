# 12. 기초 - 반복실행구조

# [71] 정수가 순서대로 입력된다. (단, 개수는 알 수 없다.) 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
def function(num, i):
    if num[i] == 0:
        return
    print(num[i])
    i += 1
    function(num, i)


num = list(map(int, input().split()))
function(num, i=0)

# [72] n개의 정수가 순서대로 입력된다. (단 n의 최대 개수는 알 수 없다.)
#  방법1
n = int(input())
num = list(map(int, input().split()))


def function(num, n, i):
    if i == n:
        return
    print(num[i])
    i += 1
    function(num, n, i)


# 방법2
n = int(input())
num = list(map(int, input().split()))
num.reverse()


def function(num, n):
    print(num[n])
    n -= 1
    if n == -1:
        return
    function(num, n)


num(num, n-1)

# [73] 정수가 순서대로 입력된다. (단, 개수는 알 수 없다.)
# 방법1
num = map(int, input().split())
for i in num:
    if num == 0:
        break
    print(num)
# 방법2
num = map(int, input().split())
for j in num:
    if j is not 0:
        print(j)
        continue
    break

# [74] 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
num = int(input())
for i in range(num, 0, -1):
    print(i)

# [75] 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
num = int(input())
for i in range(num, -1, -1):
    print(i)

# [76] 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.
char = ord(input())
# 97 ='a'
for i in range(97, char+1):
    print(chr(i), end=' ')
    # end=' ' : 마지막에 개행이 아닌 공백을 주겠다

# [77] 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
# for
num = int(input())
for i in range(0, num+1):
    print(i)

# while
num = int(input())
i = 0
while num >= 0:
    print(i)
    i += 1
    num -= 1
