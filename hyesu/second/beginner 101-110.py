# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# bool 타입입니다.


# 102
# 아래 코드의 출력 결과를 예상하라.
print(3 == 5)
# False


# 103
# 아래 코드의 출력 결과를 예상하라.
print(3 < 5)
# True


# 104
# 아래 코드의 결과를 예상하라.
x = 4
print(1 < x < 5)
# True


# 105
# 아래 코드의 결과를 예상하라.
print ((3 == 3) and (4 != 3))
# True


# 106
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
print(3 => 4)
# 기호가 잘못됨. 지원하지 않는 연산자입니다.


# 107
# 아래 코드의 출력 결과를 예상하라.
if 4 < 3:
    print("Hello World")
# 조건을 만족하지 않기 때문에 아무 결과도 출력되지 않습니다.


# 108
# 아래 코드의 출력 결과를 예상하라.
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# 조건을 만족하지 않기 때문에 else에서 들여쓰기 된 문장이 실행됩니다.
# Hi, there.


# 109
# 아래 코드의 출력 결과를 예상하라.
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1 2 4


# 110
# 아래 코드의 출력 결과를 예상하라.
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 3 5


