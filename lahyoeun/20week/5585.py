money = int(input())
count = 0
charge = [500, 100, 50, 10, 5, 1]
a = 1000-money
for i in charge:
    if a > 0:
        count += a // i
        a = a % i
print(count)
