n = int(input())
num = list(map(int, input().split()))
m = int(input())
count = 0
for i in num:
    if i == m:
        count += 1
print(count)
