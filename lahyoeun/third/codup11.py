'''
[65]

세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
'''
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)


'''
[66]

세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
'''
a, b, c = map(int, input().split())
print('odd' if a % 2 else 'even')  # odd를 출력하라 a%2의 값이 참일때, 아니면 even 출력
print('odd' if b % 2 else 'even')
print('odd' if c % 2 else 'even')


'''
[67]

정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
'''
num = int(input())
print(num > 0 and 'plus' or 'minus')
print(num % 2 and 'odd' or 'even')


'''
[68]

점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

**평가 기준**
점수 범위 : 평가
 90 ~  100 : A
 70 ~   89 : B
 40 ~   69 : C
  0 ~   39 : D
로 평가되어야 한다.
'''
i = int(input())
if i >= 90:
    print("A")
if i >= 70:
    print("B")
if i >= 40:
    print("C")
else:
    print("D")


'''
[69]

평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
[평가 : 내용]
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
'''
i = input()
if i == "A":
    print("best!!!")
if i == "B":
    print("good!!")
if i == "C":
    print("run!")
if i == "D":
    print("slowly~")
else:
    print("what?")


'''
[70] 

월이 입력될 때 계절 이름이 출력되도록 해보자.
'''
month = int(input())
if month == 12 or month == 1 or month == 2:
    print('winter')
elif month == 3 or month == 4 or month == 5:
    print('spring')
elif month == 6 or month == 7 or month == 8:
    print('summer')
else:
    print('fall')
