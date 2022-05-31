# [11098] 첼시를 부탁해
n = int(input())
for _ in range(n):
    num = 0
    Name = ""
    p = int(input())
    for _ in range(p):
        number, name = input().split()
        if int(number) > num:
            num = int(number)
            Name = name
    print(name)
