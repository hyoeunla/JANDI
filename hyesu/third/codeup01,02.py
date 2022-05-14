# [1] Hello 출력하기
print('Hello')

# [2]Hello World 출력하기
print('Hello world')

'''
[3]
Hello
World
(두 줄에 걸쳐 줄을 바꿔 출력하기)
'''
print('''\
Hello
World
''')

# [4] 'Hello' (단, 작은 따옴표도 함께 출력한다.)
print("Hello")

# [5] "Hello World" (단, 큰따옴표도 함께 출력한다.)
print('"Hello world"')

# [6] "!@#$%^&*()" (단, 큰따옴표도 함께 출력한다.)
print('"!@#$%^&*()"')

# [7] "C:\Download\hello.cpp" (단, 큰따옴표도 함께 출력한다.)
print('"C:\Download\hello.cpp"')

'''
[8]
┌┬┐
├┼┤
└┴┘
출력하기
'''
print('''\
┌┬┐
├┼┤
└┴┘
''')


# [10] 정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.
var = int(input())
print(var)

# [11] 문자형(char)으로 변수를 하나 선언하고, 변수에 문자를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.
var = input()
print(var)

# [12] 실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후 저장되어 있는 실수값을 출력해보자.
var = float(input())
print(var)

'''
[13]
정수(int) 2개를 입력받아 그대로 출력해보자. (단, 띄어쓰기를 기준으로 입력한다.)
입력 : 1 5
출력 : 1 5
'''
var = list(map(int, input().split()))
print(var[0], var[1])

# [14] 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
var = int().split()
print(var[1], var[0])

# [15] 실수(float) 1개를 입력받아 저장한 후, 저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여 소수점 이하 둘 째 자리까지 출력하시오.

var = int(input(), 2)
print(var, var, var)

# [16] int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.
var = int(input())
print(var, var, var)

'''
[17]
어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
콜론(:) 기호를 기준으로 두 수가 각 변수에 저장된다.

입력 : 3:15
출력 : 3:15
'''
h, m = input().split(':')
print('{}:{}'.format(h, m))

'''
[17]
어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
콜론(:) 기호를 기준으로 두 수가 각 변수에 저장된다.

입력 : 3:15
출력 : 3:15
'''
y, m, d = input().split('.')
if len(m) == 1:
    m = '0'+m
if len(d) == 1:
    d = '0'+d
print('{}.{}.{}'.format(y, m, d))

'''
[19]
주민번호는 다음과 같이 구성된다.

XXXXXX-XXXXXXX

앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류검출코드이다.
주민번호를 입력받아 형태를 바꿔 출력해보자.

입력
주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다. (입력값은 가상의 주민번호이다.) ex)110011-0000000
출력
'-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.

입력 : 000907-1121112
출력 : 0009071121112
'''
a, b = input().split('-')
print('{}{}'.format(a, b))


# [20] 1개의 문자열을 입력받아 그대로 출력해보자.
string = input()
print(string)

# [22] 공백이 포함되어 있는 한 문장이 입력된다. 단, 입력되는 문장은 여러 개의 단어로 구성되고, 엔터로 끝난다.
string = input()
print(string)

'''
[23]
실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.

입력 :
1.435867

출력 :
1
435867
'''
string = input().split('.')
print('''\
{}
{}
'''.format(string[0], string[1]))

'''
[24]
단어를 1개 입력받는다.
입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.
(단, 단어의 문자(영어)를 하나씩 나누어 한 줄에 한 개씩 ' '로 묶어서 출력한다.)

입력 :
'Boy'

출력 :
'B'
'o'
'y'
'''
string = input()
for i in range(len(string)):
    print("'{}'".format(string[i]))

'''
[25]
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.

입력 :
75254

출력 :
[70000]
[5000]
[200]
[50]
[4]
'''
integer = input()
count = len(integer)-1
for i in range(len(integer)):
    print([int(integer[i] + '0' * count)])


# [26] 입력되는 시:분:초 에서 분만 출력해보자.
h, m, s = input().split(':')
print(m)

'''
[27]
년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.

년월일(yyyy.mm.dd)를 입력받아,

일월년(dd-mm-yyyy)로 출력해보자.

(단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)
'''
y, m, d = input().split('.')
m = '0' + m if len(m) == 1 else m
d = '0' + d if len(d) == 1 else d
print('{}-{}-{}'.format(d, m, y))
