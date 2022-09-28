# 12933. 정수 내림차순으로 배치하기
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))

# sorted로 감싸면 list형으로 변환되어 나오므로 list를 안 적어도 된다.