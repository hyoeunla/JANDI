# 내 풀이
x, y = map(int, input().split())
if x == 1:
    if y % 7 == 1:
        print("MON")
    elif y % 7 == 2:
        print("TUE")
    elif y % 7 == 3:
        print("WED")
    elif y % 7 == 4:
        print("THU")
    elif y % 7 == 5:
        print("FRI")
    elif y % 7 == 6:
        print("SAT")
    elif y % 7 == 0:
        print("SUN")

elif x == 2:
    if y % 7 == 1:
        print("THU")
    elif y % 7 == 2:
        print("FRI")
    elif y % 7 == 3:
        print("SAT")
    elif y % 7 == 4:
        print("SUN")
    elif y % 7 == 5:
        print("MON")
    elif y % 7 == 6:
        print("TUE")
    elif y % 7 == 0:
        print("WED")

elif x == 3:
    if y % 7 == 1:
        print("THU")
    elif y % 7 == 2:
        print("FRI")
    elif y % 7 == 3:
        print("SAT")
    elif y % 7 == 4:
        print("SUN")
    elif y % 7 == 5:
        print("MON")
    elif y % 7 == 6:
        print("TUE")
    elif y % 7 == 0:
        print("WED")

elif x == 4:
    if y % 7 == 1:
        print("SUN")
    elif y % 7 == 2:
        print("MON")
    elif y % 7 == 3:
        print("TUE")
    elif y % 7 == 4:
        print("WED")
    elif y % 7 == 5:
        print("THU")
    elif y % 7 == 6:
        print("FRI")
    elif y % 7 == 0:
        print("SAT")

elif x == 5:
    if y % 7 == 1:
        print("TUE")
    elif y % 7 == 2:
        print("WED")
    elif y % 7 == 3:
        print("THU")
    elif y % 7 == 4:
        print("FRI")
    elif y % 7 == 5:
        print("SAT")
    elif y % 7 == 6:
        print("SUN")
    elif y % 7 == 0:
        print("MON")

elif x == 6:
    if y % 7 == 1:
        print("FRI")
    elif y % 7 == 2:
        print("SAT")
    elif y % 7 == 3:
        print("SUN")
    elif y % 7 == 4:
        print("MON")
    elif y % 7 == 5:
        print("TUE")
    elif y % 7 == 6:
        print("WED")
    elif y % 7 == 0:
        print("TRU")

elif x == 7:
    if y % 7 == 1:
        print("SUN")
    elif y % 7 == 2:
        print("MON")
    elif y % 7 == 3:
        print("TUE")
    elif y % 7 == 4:
        print("WED")
    elif y % 7 == 5:
        print("THU")
    elif y % 7 == 6:
        print("FRI")
    elif y % 7 == 0:
        print("SAT")

elif x == 8:
    if y % 7 == 1:
        print("WED")
    elif y % 7 == 2:
        print("TRU")
    elif y % 7 == 3:
        print("FRI")
    elif y % 7 == 4:
        print("SAT")
    elif y % 7 == 5:
        print("SUN")
    elif y % 7 == 6:
        print("MON")
    elif y % 7 == 0:
        print("TUE")

elif x == 9:
    if y % 7 == 1:
        print("SAT")
    elif y % 7 == 2:
        print("SUN")
    elif y % 7 == 3:
        print("MON")
    elif y % 7 == 4:
        print("TUE")
    elif y % 7 == 5:
        print("WED")
    elif y % 7 == 6:
        print("TRU")
    elif y % 7 == 0:
        print("FRI")

if x == 10:
    if y % 7 == 1:
        print("MON")
    elif y % 7 == 2:
        print("TUE")
    elif y % 7 == 3:
        print("WED")
    elif y % 7 == 4:
        print("THU")
    elif y % 7 == 5:
        print("FRI")
    elif y % 7 == 6:
        print("SAT")
    elif y % 7 == 0:
        print("SUN")

elif x == 11:
    if y % 7 == 1:
        print("THU")
    elif y % 7 == 2:
        print("FRI")
    elif y % 7 == 3:
        print("SAT")
    elif y % 7 == 4:
        print("SUN")
    elif y % 7 == 5:
        print("MON")
    elif y % 7 == 6:
        print("TUE")
    elif y % 7 == 0:
        print("WED")

elif x == 12:
    if y % 7 == 1:
        print("SAT")
    elif y % 7 == 2:
        print("SUN")
    elif y % 7 == 3:
        print("MON")
    elif y % 7 == 4:
        print("TUE")
    elif y % 7 == 5:
        print("WED")
    elif y % 7 == 6:
        print("TRU")
    elif y % 7 == 0:
        print("FRI")

# 다른 사람 풀이
month, day = input().split()
month = int(month)
day = int(day)

for i in range(1, month):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        day += 31
    elif i == 2:
        day += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        day += 30

day %= 7
if day == 0:
    print("SUN")
elif day == 1:
    print("MON")
elif day == 2:
    print("TUE")
elif day == 3:
    print("WED")
elif day == 4:
    print("THU")
elif day == 5:
    print("FRI")
elif day == 6:
    print("SAT")
