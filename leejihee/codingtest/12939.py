# 12939. 최솟값과 최댓값
def solution(s):
    arr = list(map(int, s.split(" ")))
    return str(min(arr)) + " " + str(max(arr))