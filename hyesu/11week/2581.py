# 소수

a = int(input())
b = int(input())

num = list(range(2, b+1))

for i in num:
    for j in num:
        if i != j and j % i == 0:
            num.remove(j)

while len(num) > 0 and num[0] < a:
    num = num[1:]

if not num:
    print(-1)
else:
    print(sum(num))
    print(min(num))
