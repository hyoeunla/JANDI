# 2. 기초-입출력

# [10] 정수형(int으로 변수를 선언하고 변수에 정수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.
num = input()
print(int(num))

# [11] 문자형(char)으로 변수를 하나 선언하고 변수에 문자를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.
char = input()
print(char)

# [12] 실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후 저장되어 있는 실수값을 출력해보자.
fNum = float(input())
print(fNum)

# [13] 정수(int) 2개를 입력받아 그대로 출력해보자.(단, 띄어쓰기를 기준으로 입력한다.)
a, b = map(int, input().split())
print(a, b)

# [14] 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
code = input().split()
print(code[1], code[0])

# [15] 실수(float) 1개를 입력받아 저장한 후, 저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여 소수점 이하 둘 째 자리까지 출력하시오.
fNum = float(input())
print(round(fNum, 2))

# [16] int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.
num = int(input())
print(num, num, num)

# [17] 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자. 클론 기호를 기준으로 두 수가 각 변수에 저장된다.
a, b = input().split(':')
print('{}:{}'.format(a, b))

''' [18] 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자
    입력 : 2020.2.9
    출력 : 2020.02.09
    (단, m 혹은 d가 한 자리 수인 경우 앞에 0을 붙여 출력한다.)'''
y, m, d = input().split('.')
if (len(m) == 1):
    m = '0'+m
if(len(d) == 1):
    d = '0'+d
print('{}.{}.{}'.format(y, m, d))

''' [19] 주민번호는 XXXXXX-XXXXXXX로 구성된다. 앞의 6자리는 생년월일이고 뒤 7자리는 성별, 지역, 오류검출코드이다. 주민번호를 입력받아 형태를 바꿔 출력해보자.
    입력 : 주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다.
        123456-7654321
    출력 : '-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.
        1234567654321'''
number = input().split('-')
print('{}{}'.format(number[0], number[1]))

# [20] 1개의 문자열을 입력받아 그대로 출력해보자.
char = input()
print(char)

# [22] 공백이 포함되어 있는 한 문장이 입력된다. 단, 입력되는 문장은 여러 개의 단어로 구성되고, 엔터로 끝난다.
char = input()
print(char)

# [23] 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
num = input().split('.')
print(num[0])
print(num[1])

print('''\
    {}
    {}
    '''.format(num[0], num[1]))

# [24] 단어를 1개 입력받는다. 입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.(단, 단어의 문자(여엉)를 하나씩 나누어 한 줄에 한 개씩 ''로 묶어서 출력한다.)
char = input()
for i in len(char):
    print(char[i])

# [25] 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
num = input()
a = len(num)-1
for i in len(num):
    print(num[i] + 'o'*a)
    a -= 1

# [26] 입력되는 시:분:초에서 분만 출력해보자.
h, m, s = input().split(':')
print(m)

''' [27] 년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다. 
년월일(yyyy.mm.dd)를 입력받아, 일월년(dd-mm-yyyy)로 출력해보자.
(단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)'''
y, m, d = input().split('.')
if(len(m) == 1):
    m = '0'+m
if(len(d) == 1):
    d = '0'+d
print('{}-{}-{}'.format(d, m, y))
