'''
53번: 1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
'''
a = int(input("정수 1개를 입력해주세요: "))
print(not a)


'''
54번: 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
'''
# 내답
# a, b = map(int, input("정수 2개를 입력해주세요: ").split())
# if a == True and b == True:
#     print(True)
# else:
#     print(False)

# 다른 방법

a, b = map(int, input("정수 2개를 입력해주세요: ").split())
if bool(a) == True and bool(b) == True:
    print(True)
else:
    print(False)

# 차이점
'''
내가 사용한 방식으로는 int로 받은 값과 True와 비교가 된다.(ex. int 3 == True) 이와 같이 비교가 되기때문에 1을 입력한 상황을 제외하고 식이 성립할 수
없기 때문에 모두 False로 출력된다. 그렇기에 다른 방법에서 사용한 bool()자료형을 사용해 int로 입력 받은 값을 True와 False로 변환시켜 비교해야 정상적으로
프로그램이 작동하게 되는 것이다.
'''


'''
55번: 두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input("정수 두개를 입력해주세요: ").split())
if bool(a) == True or bool(b) == True:
    print(True)
else:
    print(False)

'''
56번: 두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
'''


a, b = map(int, input("정수 두개를 입력해주세요: ").split())
if (a and (not b)) or ((not a) and b):
    print(True)
else:
    print(False)

'''
57번: 두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
'''
a, b = map(int, input("정수 두개를 입력해주세요: ").split())
if bool(a) == bool(b):
    print(True)
else:
    print(False)

'''
58번: 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
'''
a, b = map(int, input("정수 두개를 입력해주세요: ").split())
if bool(a) == False and bool(b) == False:
    print(True)
else:
    print(False)

'''
다른 방법
'''
a, b = map(int, input().split())
print(not(a or b))

'''
차이점: 내가 사용한 방식과 다른 방법이 서로 의미는 같지만 사용한 방식이 다르다. 내가 사용한 방식은 bool()로 자료형을 변환시켜 직접 True, False 와
비교하는 것이고, 다른 방법에선 a=0, b=0 일때 참이 출력 됨으로 not a and not b 일때 참이 출력이 되는 것이다. 이를 정리하면 not(a or b)가 된다.
'''
