# 12935. 제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    return [-1] if len(arr) == 0 else arr