n = input()
count = 0
result = 0
c = int(n)
if c == 0:
    print(1)
else:
    if int(n) >= 10:
        while int(n) != result:
            a = c//10
            b = c % 10
            c = b*10 + ((a+b) % 10)
            count += 1
            result = c

    else:
        a = 0
        b = c
        while int(n) != result:
            c = b*10 + ((a+b) % 10)
            a = c//10
            b = c % 10
            count += 1
            result = c

    print(count)
