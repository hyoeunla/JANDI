t = int(input())
for i in range(t):
    r, s = input().split()
    s = list(s)
    for j in s:
        print(j*int(r), end='')
    print()
