# 2007년

sum = 0
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

m, d = map(int, input().split())

for i in range(1, m):
    if i in a:
        sum += 31
    elif i in b:
        sum += 30
    elif i == 2:
        sum += 28

sum += d
print(week[sum % 7])
