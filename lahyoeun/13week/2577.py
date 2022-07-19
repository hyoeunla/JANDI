# 내 풀이
a = int(input())
b = int(input())
c = int(input())
num = []
count = [0] * 10
mul = a * b * c

while mul != 0:
    num.append(mul % 10)
    mul = mul//10
for i in num:
    if i == 0:
        count[0] += 1
    elif i == 1:
        count[1] += 1
    elif i == 2:
        count[2] += 1
    elif i == 3:
        count[3] += 1
    elif i == 4:
        count[4] += 1
    elif i == 5:
        count[5] += 1
    elif i == 6:
        count[6] += 1
    elif i == 7:
        count[7] += 1
    elif i == 8:
        count[8] += 1
    elif i == 9:
        count[9] += 1
for i in range(10):
    print(count[i])

# 다른 사람 풀이
a = int(input())
b = int(input())
c = int(input())
mult = a*b*c
digit = 0
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while mult > 0:
    digit = mult % 10
    count[digit] += 1
    mult //= 10
for i in count:
    print(i)
