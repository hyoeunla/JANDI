# 문제8. 만들 수 없는 금액

n = int(input())
num = list(map(int, input().split()))
num.short()

target = 1
for i in num:
    if target < i:
        break
    target += i
print(target)
