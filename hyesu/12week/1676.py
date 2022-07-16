# 팩토리얼 0의 개수

n = int(input())
f = 1
factorial = []
count = 0
for i in range(1, n+1):
    f = f * i

for j in str(f):
    factorial.append(j)

while True:
    if factorial[-1] == '0':
        factorial.pop(-1)
        count += 1

    else:
        break

print(count)
