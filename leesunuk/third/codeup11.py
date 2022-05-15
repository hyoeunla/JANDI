'''
65번: 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
'''
a, b, c = map(int, input("정수 3개를 입력해주세요: ").split())

if a % 2 == 0:
    print(a)
if b & 1 != 1:
    print(b)
if c % 2 != 1:
    print(c)

'''
66번: 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
'''
a, b, c = map(int, input("정수 3개를 입력해주세요: ").split())

if a % 2 == 0:
    print("even")
else:
    print("odd")
if b & 1 != 1:
    print("even")
else:
    print("odd")
if c % 2 != 1:
    print("even")
else:
    print("odd")

'''
67번: 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
'''

a = int(input("정수 1개를 입력해주세요: "))

if a > 0:
    print("plus")
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("minus")
    if a & 1 != 1:
        print("even")
    else:
        print("odd")

'''
다른 방법 (and or 를 사용하는 방법)
'''
a = int(input("정수 1개를 입력해주세요: "))
print(a > 0 and "plus" or "minus")
print(a % 2 == 0 and "even" or "odd")

'''
68번: 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

**평가 기준**
점수 범위 : 평가
 90 ~  100 : A
 70 ~   89 : B
 40 ~   69 : C
  0 ~   39 : D
로 평가되어야 한다.
'''

test = int(input("점수를 입력해주세요: "))
if test >= 90:
    print("A")
elif test >= 70:
    print("B")
elif test >= 40:
    print("C")
else:
    print("D")

'''
69번: 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

[평가 : 내용]
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
'''

a = input("영 문자 하나를(A~D까지 중 하나) 입력해주세요: ")
if a == "A":
    print("best!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

'''
70번: 월이 입력될 때 계절 이름이 출력되도록 해보자.

[월 : 계절 이름]
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall
'''

a = int(input("몇월인지 입력해주세요: "))

if a == 12 or a == 1 or a == 2:
    print("winter")
elif a == 3 or a == 4 or a == 5:
    print("spring")
elif a == 6 or a == 7 or a == 8:
    print("summer")
elif a == 9 or a == 10 or a == 11:
    print("fall")
else:
    print("1~12 중의 숫자로 다시 입력해주세요")
