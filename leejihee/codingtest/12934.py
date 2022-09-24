def solution(n):
    root = n ** (1/2)
    return (root+1)**2 if root % 1 == 0 else -1