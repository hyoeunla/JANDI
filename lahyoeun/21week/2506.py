n = int(input())
num = list(map(int, input().split()))
point = 0
addpoint = 0
for i in range(n):
    if num[i] == 1:
        point = point + addpoint + 1
        addpoint += 1
    else:
        addpoint = 0
print(point)
