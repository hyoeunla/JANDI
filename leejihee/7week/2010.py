# 2010. 플러그
n = int(input())
result = 0

for _ in range(n):
    p = int(input())
    result += p
result -= (n-1)  # 연결되는 코드는 하나씩 빼줘야하는데 마지막은 연결이 필요없으므로 -1빼줌
print(result)
