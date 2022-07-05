# 1924. 2007년
# 나의 풀이
x, y = map(int, input().split())

for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        y += 31
    elif i in [4, 6, 9, 11]:
        y += 30
    elif i in [2]:
        y += 28

if y % 7 == 1:
    print('MON')
elif y % 7 == 2:
    print('TUE')
elif y % 7 == 3:
    print('WED')
elif y % 7 == 4:
    print('THU')
elif y % 7 == 5:
    print('FRI')
elif y % 7 == 6:
    print('SAT')
elif y % 7 == 0:
    print('SUN')

# 다른 풀이
week = ['SUN', 'MON', 'TUE', 'WED', 'TUR', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
day = 0

for i in range(x-1):  # 입력한 달은 제외
    day += month[i]

day = (day+y) % 7
print(week[day])
