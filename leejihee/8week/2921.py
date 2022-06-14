# 2921. 도미노
# 조합을 이용한 문제
n = int(input())
a = 0
# (0,1)과 (1,0)을 같은 취급하므로 (1,1)부터 시작해야함
# 위와 같은 상황이 반복되어 j는 계속 하나씩 밀려남
result = 0

for i in range(0, n+1):
    for j in range(a, n+1):
        result += i
        result += j
    a += 1
print(result)
