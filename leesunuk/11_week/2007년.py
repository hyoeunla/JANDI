# 백준 1924번 문제: 2007년

M, D = map(int, input().split())
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
shortday = [4, 6, 9, 11]
result = 0
if M > 1:
    for i in range(1, M):
        if i in shortday:
            D += 30
        elif i == 2:
            D += 28
        else:
            D += 31
    result = (D % 7)
else:
    if D > 7:
        result = D % 7
    else:
        result = D
print(days[result])
