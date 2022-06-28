def solution(s):
    # join 으로 붙이기, sort로 정렬 후 반대로 뒤집기
    answer = ''.join(sorted(s, reverse=True))
    return answer
