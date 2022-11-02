# 12947. 하샤드 수
# 나의 풀이
def solution(x):
    div = sum(list(map(int, str(x))))
    return True if x % div == 0 else False

# 다른 사람 풀이
def solution(n):
    return n % sum([int(i) for i in str(n)]) == 0  #0이면 True, 아니면 False