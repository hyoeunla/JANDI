# 70128. 내적
def solution(a, b):
    return sum(i*j for i, j in zip(a,b))