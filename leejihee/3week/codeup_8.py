'''
[53]
1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
'''
a = int(input())
print(not a)

'''
[54] ★
두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())  # 참은 0이 아닌 수
if a != 0 and b != 0:
    print(a, b)
else:
    print('false값이 있음')


'''    
[55]
두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())  # 참은 0이 아닌 수
if a and b:  # a만 쓰면 참이다
    print(a, b)
elif a or b:
    print(a or b)
else:
    print('둘 다 false')

'''
[우리밋이 알려주는 Bonus 문제 (1)]
1개의 정수형 입력이 들어오면 논리 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
'''
# 나의 풀이
a = int(input())
if a % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 의도한 풀이
a = int(input())
print(a % 2 and '홀수' or '짝수')
# 5이면 true and true이므로 뒤의 값을 출력해서 홀수
# 8이면 false and true이므로 0(false)출력, false or true이므로 뒤의 값을 출력해서 짝수

'''
[56]
두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
print((a and (not b)) or ((not a) and b))
# 1,0이면 (1 and 1) or (0 and 0) = true or false = ture
# 1,1이면 (1 and 0) or (0 and 1) = false or false = false

'''
[57]
두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
print(((not a) and (not b)) or (a and b))

'''
[58]
두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
print(not(a or b))
