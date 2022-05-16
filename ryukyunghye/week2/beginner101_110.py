# 101. 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# bool 타입

# 102. 아래 코드의 출력 결과를 예상하라
print(3 == 5)
# false

# 103. 아래 코드의 출력 결과를 예상하라
print(3 < 5)
# true

# 104. 아래 코드의 출력 결과를 예상하라
x = 4
print(1 < x < 5)
# true

# 105. 아래 코드의 출력 결과를 예상하라
print((3 == 3) and (4 != 3))
# true

# 106. 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3=>4)
print(3 >= 4)
# =>이 아닌 >=를 사용해야 한다(지원 안 함)

# 107. 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World")
# 조건문에 만족X -> 출력 결과X

# 108. 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World")
else:
    print("Hi, there.")
# Hi, there.

# 109. 아래 코드의 출력 결과를 예상하라
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")
# 1 2 4

# 110. 아래 코드의 출력 결과를 예상하라
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
# 3 5
