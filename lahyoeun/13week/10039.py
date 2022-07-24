hap = 0
for i in range(5):
    n = int(input())
    if n < 40:
        hap += 40
    else:
        hap = hap + n
print(hap//5)
