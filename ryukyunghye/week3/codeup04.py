# 4. 기초 - 출력 변환

# [31] 10진수를 입력받아 8진수로 출력해보자.
num = int(input())
print(oct(num)[2:])
# oct() : 10진수를 8진수로 변환
# [2:] : 앞에 0o을 생략하고 숫자만 출력

# [32] 10진수를 입력받아 16진수로 출력해보자.
num = int(input())
print(hex(num)[2:])
# hex() : 10진수를 16진수로 변환

# [33] 10진수를 입력받아 16진수로 출력해보자. 16진수(대문자)로 출력한다.
num = int(input())
print(hex(num)[2:].upper())

# [34] 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
num = +'0o'+input()
print(int(num, 8))
# int(x ,n) : 변수 x를 n진수로 변환

# [35] 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
num1 = '0o'+input()
num2 = int(num1, 16)
print(oct(num2)[2:])

# [36] 영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.
char = input()
print(ord(char))
# ord() : 문자열에 대응되는 아스키코드 반환

# [37] 10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
num = int(input())
print(ord(num))
