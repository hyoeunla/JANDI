# '''
# 53번: 1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
# '''
# a = int(input("정수 1개를 입력해주세요: "))
# print(not a)


# '''
# 54번: 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
# '''
# a, b = map(int, input("정수 2개를 입력해주세요: ").split())
# if bool(a) == True and bool(b) == True:
#     print(True)
# else:
#     print(False)

# '''
# 55번: 두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
# '''
# a, b = map(int, input("정수 두개를 입력해주세요: ").split())
# if bool(a) == True or bool(b) == True:
#     print(True)
# else:
#     print(False)

# '''
# 56번: 두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
# '''


# a, b = map(int, input("정수 두개를 입력해주세요: ").split())
# if (a and (not b)) or ((not a) and b):
#     print(True)
# else:
#     print(False)

'''
57번: 두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
'''
a, b = map(int, input("정수 두개를 입력해주세요: ").split())
if bool(a) == bool(b):
    print(True)
else:
    print(False)
