# [2921] 도미노
# (N+1) *1.5
N = int(input())
result = 0
for i in range(1, N+1):
    result += 1.5*i*(i+1)
print(int(result))
