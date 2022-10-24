# 하샤드 수

def solution(x):
    result = [int(i) for i in str(x)]
    if x % sum (result) == 0:
        return True
    else:
        return False