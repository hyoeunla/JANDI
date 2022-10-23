l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c != 0:
    day = (a//c) + 1
else:
    day = (a//c)
if b % d != 0:
    day1 = (b//d) + 1
else:
    day1 = (b//d)

if day > day1:
    day = day
else:
    day = day1

print(l-day)
