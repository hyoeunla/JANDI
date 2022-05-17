'''
[31]
10진수를 입력받아 8진수(octal)로 출력해보자.
'''
a = int(input())
print( oct(a)[2:] )

'''
[32]
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
'''
h = int(input())
print( hex(h)[2:] )

'''
[33]
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
16진수(대문자)로 출력한다.
'''
hexadecimal = int(input())
hexConv = hex(hexadecimal)[2:]
print( hexConv.upper() )

'''
[34]
8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
'''
a = '0o' + input()
print( int(a, 8) )

'''
[35]
16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
'''
hexadecimal = '0x' + input()
integer = int(hexadecimal, 16)
print( oct(integer)[2:] )

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

