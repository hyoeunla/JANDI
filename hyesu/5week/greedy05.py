# 문제5. 모험가 길드

n = int(input())

num = list(map(int, input.split()))
num.short()

result = 0
count = 0

for i in num:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
