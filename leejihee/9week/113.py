# 4-2. 시각
n = int(input())
result = 0

for i in range(n+1):  # 0시 ~ n시 59분 59초
    for j in range(60):
        for k in range(60):
            # print(i, ':', j, ':', k) 모든 수를 나타냄
            if '3' in str(i)+str(j)+str(k):
                result += 1
print(result)
