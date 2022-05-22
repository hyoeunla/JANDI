'''
[31]
10진수를 입력받아 8진수(octal)로 출력해보자.
'''
octal = int(input())
print(oct(octal)[2:])


'''
[32]
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
'''
hexadecimal = int(input())
print(hex(hexadecimal)[2:])


'''
[33]
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
16진수(대문자)로 출력한다.
'''
hexadecimal = int(input())
hexUP = hex(hexadecimal)[2:]
print(hexUP.upper())


'''
[34]
8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
'''
octal = '0o' + input()
print(int(octal, 8))


'''
[35]
16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
'''
hexadecimal = '0x' + input()
octal = int(hexadecimal, 16)
print(oct(octal)[2:])


'''
[36]
영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.
'''
a = ord(input())
print(a)


'''
[37]
10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
'''
a = chr(int(input()))
print(a)
