n = int(input())
num = []
count = 0
while n != 0:
    while n != 0:
        num.append(n % 10)
        n = n//10

    for i in range(len(num)):
        if num[i] == 0:
            count += 4
        elif num[i] == 1:
            count += 2
        else:
            count += 3
    print(count+(len(num)+1))
    count = 0
    num = []
    n = int(input())
