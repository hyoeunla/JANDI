# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# 정답: bool

# 102
# 아래 코드의 출력 결과를 예상하라
print(3 == 5)
#정답: False

# 103
# 아래 코드의 출력 결과를 예상하라
print(3 < 5)
# 정답: True

# 104
# 아래 코드의 결과를 예상하라.
x = 4
print(1 < x < 5)
# 정답: True

# 105
# 아래 코드의 결과를 예상하라.
print((3 == 3) and (4 != 3))
# 정답: 3==3은 true, 4!=3은 true, and연산자는 둘 다 true이면 true가 된다.

'''
106
아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
print(3= > 4)
정답: 연산자가 >=가 되어야 함
'''

# 107
# 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World")
# 정답: 조건이 false이므로 실행되지 않는다.

# 108
# 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# 정답: Hi, there.

# 109
# 아래 코드의 출력 결과를 예상하라
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")
# 정답: 조건이 true이므로 1,2가 출력되고 4가 출력된다.

# 110
# 아래 코드의 출력 결과를 예상하라
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
# 정답: 3 5
