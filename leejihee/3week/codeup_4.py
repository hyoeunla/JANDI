'''
[31]
10진수를 입력받아 8진수(octal)로 출력해보자.
'''
a = int(input())
print(oct(a)[2:])

''' 
[32]
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
'''
a = int(input())
print(hex(a)[2:])

'''
[33]
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
16진수(대문자)로 출력한다.
'''
a = int(input())
hex_a = hex(a)[2:]
print(hex_a.upper())

'''
[34]
8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
'''
a = '0o'+input()
print(int(a, 8))

''' 
[35]
16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
'''
a = '0x' + input()
int_a = int(a, 16)
print(oct(int_a)[2:])

'''
[36]
영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.
'''
a = input()
print(ord(a))

'''
[37]
10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
'''
a = int(input())
print(chr(a))
