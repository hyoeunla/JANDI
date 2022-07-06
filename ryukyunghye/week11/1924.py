# 2007년
dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0
m, d = map(int, input().split())
for i in range(m-1):
    day += dayList[i]
day = (day+d) % 7
print(weekList[day])
