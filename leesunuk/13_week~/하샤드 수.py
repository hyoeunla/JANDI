# 하샤드 수

def solution(x):
    result = 0
    a = x
    b = x

    x = x//10
    x = str(x)
    for i in list(x):
        result += int(i)
    b %= 10
    result += b
    if a % result == 0:
        return True
    else:
        return False
