# 시각

h = int(input())  # h를 압력받기

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):   # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                count += 1

print(count)
