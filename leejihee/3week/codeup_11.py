'''
[65]
세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
'''
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:  # elif 아님
    print(b)
if c % 2 == 0:
    print(c)

'''
[66]
세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
'''
a, b, c = map(int, input().split())
print("even" if a % 2 == 0 else "odd")  # if else를 이용한 삼항연산
print(b % 2 and 'odd' or 'even')  # and or을 이용한 삼항연산
print(['even', 'odd'][c % 2])  # ★

'''
[67]
정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

입력
-4
출력
minus
even
'''
num = int(input())
print("음수" if num < 0 else "양수")
print("홀수" if num % 2 else "짝수")

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
score = int(input())
if score <= 100 and score >= 90:
    print("A")
elif score < 90 and score >= 70:
    print("B")
elif score < 70 and score >= 40:
    print("C")
elif score < 40 and score >= 0:
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
word = input()
if word == "A":
    print("best!!!")
elif word == "B":
    print("good!!")
elif word == "C":
    print("run!")
elif word == "D":
    print("slowly~")
else:
    print("what?")

'''
[70] 
월이 입력될 때 계절 이름이 출력되도록 해보자.

예
[월 : 계절 이름]
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall
'''
m = int(input())
if m in [12, 1, 2]:
    print("winter")
elif m in [3, 4, 5]:
    print("spring")
elif m in [6, 7, 8]:
    print("summer")
elif m in [9, 10, 11]:
    print("fall")
