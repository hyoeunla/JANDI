n = int(input())
count = 0
for i in range(n):
    a = input().split()
    a = list(map(int, a))
    b = a[1:len(a)]
    avg = sum(b)/len(b)
    for j in b:
        if j > avg:
            count += 1
    s = format(count/len(b)*100, ".3f")
    print(str(s)+"%")
    count = 0
