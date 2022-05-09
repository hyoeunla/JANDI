'''
151
리스트에는 네 개의 정수가 저장돼 있다.

리스트 = [3, -20, -3, 44]
for문을 사용해서 리스트의 음수를 출력하라.

-20
-3
'''
list = [3, -20, -3, 44]
for i in list:
    if(i < 0):
        print(i)

'''
152
for문을 사용해서 3의 배수만을 출력하라.

리스트 = [3, 100, 23, 44]
3
'''
list = [3, 100, 23, 44]
for i in list:
    if(i % 3 == 0):
        print(i)

'''
153
리스트에서 20 보다 작은 3의 배수를 출력하라

리스트 = [13, 21, 12, 14, 30, 18]
12
18
'''
list = [13, 21, 12, 14, 30, 18]
for i in list:
    if (i < 20 and i % 3 == 0):
        print(i)

'''
154
리스트에서 세 글자 이상의 문자를 화면에 출력하라

리스트 = ["I", "study", "python", "language", "!"]
study
python
language
'''
list = ["I", "study", "python", "language", "!"]
for i in list:
    if (len(i) >= 3):
        print(i)

'''
155
리스트에서 대문자만 화면에 출력하라.

리스트 = ["A", "b", "c", "D"]
A
D
(참고) isupper() 메서드는 대문자 여부를 판별합니다.
'''
list = ["A", "b", "c", "D"]
for i in list:
    if (i.isupper() == True):
        print(i)

'''
156
리스트에서 소문자만 화면에 출력하라.

리스트 = ["A", "b", "c", "D"]
b
c
'''
list = ["A", "b", "c", "D"]
for i in list:
    if (i.isupper() == False):
        print(i)

'''
157
이름의 첫 글자를 대문자로 변경해서 출력하라.

리스트 = ['dog', 'cat', 'parrot']
Dog
Cat
Parrot
(참고) upper() 메서드는 문자열을 대문자로 변경합니다.
'''
list = ['dog', 'cat', 'parrot']
for i in list:
    print(i[0].upper()+i[1:])

'''
158
파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
hello
ex01
intro
'''
list = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list:
    name = i.split('.')
    print(name[0])

'''
159
파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
intra.h
define.h
'''
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    name = i.split('.')
    if(name[1] == 'h'):
        print(i)

'''
160
파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
intra.h
intra.c
define.h
'''
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    name = i.split('.')
    if (name[1] == 'h' or name[1] == 'c'):
        print(i)
