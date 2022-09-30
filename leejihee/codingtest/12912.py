# 12912. 두 정수 사이의 합
# 나의 풀이
def solution(a, b):
    sum = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        sum += i
    return sum

# 다른 사람 풀이 1
def adder(a, b):
    if a > b: 
        a, b = b, a
    return sum(range(a,b+1))

# 다른 사람 풀이 2
def adder(a, b):
    return sum(range(min(a,b),max(a,b)+1))