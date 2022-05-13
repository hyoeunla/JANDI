'''
[53]

1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
'''
bool = int(input())
print( not bool )

'''
[54]

두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
print( a and b )

'''
[55]

두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
print( a or b )

'''
[56]

두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
print( (a and (not b)) or ((not a) and b))

'''
[57]

두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
print( ((not a) and (not b)) or (a and b))

'''
[58]

두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
'''
a, b = map(int, input().split())
print( not(a or b) )


