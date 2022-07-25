hap = 0
array = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        hap += n
        array.append(n)
if len(array) == 0:
    print(-1)
else:
    print(hap)
    print(min(array))
