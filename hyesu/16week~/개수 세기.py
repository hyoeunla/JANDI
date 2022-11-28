# 개수 세기

first = int(input())
a = list(map(int, input().split()))
want = int(input())
count = 0

for i in range(first):
    if a[i] == want:
        count += 1

print(count)
