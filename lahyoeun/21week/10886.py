n = int(input())
count0 = 0
count1 = 1
for i in range(n):
    s = int(input())
    if s == 1:
        count1 += 1
    else:
        count0 += 1

if count1 > count0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
